# -*- coding: utf-8 -*-
"""
    Catch-up TV & More
    Original work (C) JUL1EN094, SPM, SylvainCecchetto
    Copyright (C) 2016  SylvainCecchetto

    This file is part of Catch-up TV & More.

    Catch-up TV & More is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    Catch-up TV & More is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with Catch-up TV & More; if not, write to the Free Software Foundation,
    Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

# The unicode_literals import only has
# an effect on Python 2.
# It makes string literals as unicode like in Python 3
from __future__ import unicode_literals

from builtins import str
from codequick import Route, Resolver, Listitem, utils, Script


from resources.lib import web_utils
from resources.lib import resolver_proxy
from resources.lib import download
from resources.lib.menu_utils import item_post_treatment

import json
import re
import urlquick

# TO DO

# Info
# Add date of videos

URL_ROOT = 'http://www.lcp.fr'

URL_LIVE_SITE = URL_ROOT + '/le-direct'

URL_CATEGORIES = URL_ROOT + '/%s'

URL_VIDEO_REPLAY = 'http://play1.qbrick.com/config/avp/v1/player/' \
                   'media/%s/darkmatter/%s/'
# VideoID, AccountId

CATEGORIES = {
    'documentaires': 'Documentaires',
    'emissions': 'Emission A-Z'
}


@Route.register
def list_categories(plugin, item_id, **kwargs):
    """
    Build categories listing
    - Tous les programmes
    - Séries
    - Informations
    - ...
    """
    for category_id, category_name in list(CATEGORIES.items()):
        category_url = URL_CATEGORIES % category_id

        item = Listitem()
        item.label = category_name
        if category_id == 'documentaires':
            item.set_callback(list_videos,
                              item_id=item_id,
                              videos_url=category_url,
                              page='0')
        else:
            item.set_callback(list_programs,
                              item_id=item_id,
                              category_url=category_url)
        item_post_treatment(item)
        yield item


@Route.register
def list_programs(plugin, item_id, category_url, **kwargs):
    """
    Build programs listing
    - Journal de 20H
    - Cash investigation
    """
    resp = urlquick.get(category_url)
    root = resp.parse()

    for program_datas in root.iterfind(".//div[@class='sticky- views-row']"):
        program_label = program_datas.find(".//h2").text
        program_image = URL_ROOT + program_datas.find(".//img").get('src')
        program_url = program_datas.find(".//a").get('href')

        item = Listitem()
        item.label = program_label
        item.art['thumb'] = item.art['landscape'] = program_image
        item.set_callback(list_videos_programs,
                          item_id=item_id,
                          videos_url=program_url,
                          page='0')
        item_post_treatment(item)
        yield item


@Route.register
def list_videos_programs(plugin, item_id, videos_url, page, **kwargs):
    """
    Build programs listing
    - Journal de 20H
    - Cash investigation
    """
    resp = urlquick.get(videos_url)
    root = resp.parse()
    all_videos_link = URL_ROOT + root.findall(".//div[@class='more-link']")[0].find(".//a").get('href')

    resp2 = urlquick.get(all_videos_link + '?page=%s' % page)
    root2 = resp2.parse("main", attrs={"class": "layout-3col__left-content"})

    for video_datas in root2.iterfind(".//div[@class='views-row']"):
        video_label = video_datas.findall(".//span[@class='field-content']")[0].text
        video_image = URL_ROOT + video_datas.find(".//img").get('src')
        video_url = video_datas.find(".//a").get('href')

        item = Listitem()
        item.label = video_label
        item.art['thumb'] = item.art['landscape'] = video_image
        item.set_callback(get_video_url,
                          item_id=item_id,
                          video_url=video_url)
        item_post_treatment(item, is_playable=True, is_downloadable=True)
        yield item

    yield Listitem.next_page(item_id=item_id,
                             videos_url=videos_url,
                             page=str(int(page) + 1))


@Route.register
def list_videos(plugin, item_id, videos_url, page, **kwargs):
    """
    Build programs listing
    - Journal de 20H
    - Cash investigation
    """
    resp = urlquick.get(videos_url + '?page=%s' % page)
    root = resp.parse()

    for video_datas in root.iterfind(".//div[@class='views-row']"):
        video_label = video_datas.findall(".//span[@class='field-content']")[0].text
        video_image = URL_ROOT + video_datas.find(".//img").get('src')
        video_url = video_datas.find(".//a").get('href')

        item = Listitem()
        item.label = video_label
        item.art['thumb'] = item.art['landscape'] = video_image
        item.set_callback(get_video_url,
                          item_id=item_id,
                          video_url=video_url)
        item_post_treatment(item, is_playable=True, is_downloadable=True)
        yield item

    yield Listitem.next_page(item_id=item_id,
                             videos_url=videos_url,
                             page=str(int(page) + 1))


@Resolver.register
def get_video_url(plugin,
                  item_id,
                  video_url,
                  download_mode=False,
                  **kwargs):

    resp = urlquick.get(video_url,
                        headers={'User-Agent': web_utils.get_random_ua()},
                        max_age=-1,
                        timeout=120)

    video_id = re.compile(
        r'www.dailymotion.com/embed/video/(.*?)[\?\"]').findall(
            resp.text)[0]
    return resolver_proxy.get_stream_dailymotion(plugin, video_id,
                                                 download_mode)


@Resolver.register
def get_live_url(plugin, item_id, **kwargs):

    resp = urlquick.get(URL_LIVE_SITE,
                        headers={'User-Agent': web_utils.get_random_ua()},
                        max_age=-1)
    video_id = re.compile(
        r'www.dailymotion.com/embed/video/(.*?)[\?\"]').findall(resp.text)[0]
    return resolver_proxy.get_stream_dailymotion(plugin, video_id, False)