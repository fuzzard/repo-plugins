# -*- coding: utf-8 -*-

# GNU General Public License v3.0 (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, unicode_literals

# https://services.vrt.be/htmlview/?href=%2Fchannel%2Fs&rel=http%3A%2F%2Fservices.vrt.be%2Fchannel%2Frel%2Fchannels
CHANNELS = [
    dict(
        id='11',
        name='radio1',
        label='Radio 1',
        tagline='Altijd Benieuwd',
        website='https://radio1.be/',
        hls_128='https://live-radio-cf-vrt.akamaized.net/groupb/live/47303075-8243-434b-8199-2e62cf4dd97a/live.isml/.m3u8',
        mpeg_dash_128='https://live-radio-cf-vrt.akamaized.net/groupb/live/47303075-8243-434b-8199-2e62cf4dd97a/live.isml/.mpd',
        mp3_128='http://icecast.vrtcdn.be/radio1-high.mp3',
        mp3_64='http://icecast.vrtcdn.be/radio1-mid.mp3',
        aac_128='http://icecast.vrtcdn.be/radio1.aac',
        logo='https://radioplayer.vrt.be/iframe/img/channelLogos/radio1.png',
        backdrop='https://images.vrt.be/orig/2018/11/26/786646bd-f14b-11e8-abcc-02b7b76bf47f.jpg',
        epg_id='radio1.be',
        preset=901,
    ),
    dict(
        id='110',
        name='radio1-classics',
        label='Radio 1 Classics',
        tagline='Een eindeloze stroom aan onsterfelijke klassiekers',
        website='https://radio1.be/',
        hls_128='https://live-radio-vrt.akamaized.net/groupa/live/0a479081-ca2c-40fb-bc16-a10c8d3708c0/live.isml/.m3u8',
        mpeg_dash_128='https://live-radio-vrt.akamaized.net/groupa/live/0a479081-ca2c-40fb-bc16-a10c8d3708c0/live.isml/.mpd',
        mp3_128='http://icecast.vrtcdn.be/radio1_classics_high.mp3',
        mp3_64='http://icecast.vrtcdn.be/radio1_classics_mid.mp3',
        aac_128='http://icecast.vrtcdn.be/radio1_classics.aac',
        logo='https://radioplayer.vrt.be/iframe/img/channelLogos/radio1classics.png',
        backdrop='https://images.vrt.be/orig/2018/11/26/786646bd-f14b-11e8-abcc-02b7b76bf47f.jpg',
        epg_id='radio1classics.be',
        preset=920,
    ),
    dict(
        id='111',
        name='radio1-lagelandenlijst',
        label='Radio 1 Lage Landenlijst',
        tagline='Sterren komen, sterren gaan. Een onsterfelijke stroom Nederlandstalige klassiekers.',
        website='https://radio1.be/',
        hls_128='https://live-radio-vrt.akamaized.net/groupc/live/4023dbf7-2934-459c-8ded-f91619f58df5/live.isml/.m3u8',
        mpeg_dash_128='https://live-radio-vrt.akamaized.net/groupc/live/4023dbf7-2934-459c-8ded-f91619f58df5/live.isml/.mpd',
        mp3_128='http://icecast.vrtcdn.be/radio1_lagelanden_high.mp3',
        mp3_64='http://icecast.vrtcdn.be/radio1_lagelanden_mid.mp3',
        aac_128='http://icecast.vrtcdn.be/radio1_lagelanden.aac',
        logo='https://radioplayer.vrt.be/iframe/img/channelLogos/radio1lagelandenlijst.png',
        backdrop='https://images.vrt.be/orig/2018/11/26/786646bd-f14b-11e8-abcc-02b7b76bf47f.jpg',
        epg_id='radio1lagelandenlijst.be',
        preset=921,
    ),
    dict(
        id='22',
        name='radio2-vlaams-brabant',
        label='Radio 2 (Vlaams-Brabant)',
        tagline='De grootste familie',
        website='https://radio2.be/',
        hls_128='',
        mpeg_dash_128='',
        mp3_128='http://icecast.vrtcdn.be/ra2vlb-high.mp3',
        mp3_64='http://icecast.vrtcdn.be/ra2vlb-mid.mp3',
        aac_128='http://icecast.vrtcdn.be/ra2vlb.aac',
        logo='https://radioplayer.vrt.be/iframe/img/channelLogos/radio2vlbr.png',
        backdrop='https://images.vrt.be/orig/2014/10/29/3a06a4e4-5f6f-11e4-aec2-00163edf75b7.jpg',
        epg_id='radio2vlb.be',
        preset=902,
    ),
    dict(
        id='120',
        name='radio2-benebene',
        label='Radio 2 Bene Bene',
        tagline='De hélé dag artiesten van bij ons',
        website='https://radio2.be/',
        hls_128='https://live-radio-vrt.akamaized.net/groupc/live/8f25e0f4-5cc0-4f76-863c-32ae9ca3a5bc/live.isml/.m3u8',
        mpeg_dash_128='https://live-radio-vrt.akamaized.net/groupc/live/8f25e0f4-5cc0-4f76-863c-32ae9ca3a5bc/live.isml/.mpd',
        mp3_128='http://icecast.vrtcdn.be/radio2_benebene_high.mp3',
        mp3_64='http://icecast.vrtcdn.be/radio2_benebene_mid.mp3',
        aac_128='http://icecast.vrtcdn.be/radio2_benebene.aac',
        logo='https://radioplayer.vrt.be/iframe/img/channelLogos/radio2benebene.png',
        backdrop='https://images.vrt.be/orig/2014/10/29/3a06a4e4-5f6f-11e4-aec2-00163edf75b7.jpg',
        epg_id='radio2benebene.be',
        preset=923,
    ),
    dict(
        id='121',
        name='radio2-unwind',
        label='Radio 2 Unwind',
        tagline='Ontspannen genieten met Radio2',
        website='https://radio2.be/',
        hls_128='https://live-radio-cf-vrt.akamaized.net/groupa/live/622f7b87-f49d-4639-93ae-ca73d991c705/live.isml/.m3u8',
        mpeg_dash_128='https://live-radio-cf-vrt.akamaized.net/groupa/live/622f7b87-f49d-4639-93ae-ca73d991c705/live.isml/.mpd',
        mp3_128='http://icecast.vrtcdn.be/radio2_unwind_high.mp3',
        mp3_64='http://icecast.vrtcdn.be/radio2_unwind-mid.mp3',
        aac_128='http://icecast.vrtcdn.be/radio2_unwind.aac',
        logo='https://radioplayer.vrt.be/iframe/img/channelLogos/radio2unwind.png',
        backdrop='https://images.vrt.be/orig/2014/10/29/3a06a4e4-5f6f-11e4-aec2-00163edf75b7.jpg',
        epg_id='radio2unwind.be',
        preset=924,
    ),
    dict(
        id='31',
        name='klara',
        label='Klara',
        tagline='Blijf verwonderd',
        website='https://klara.be/',
        hls_128='https://live-radio-cf-vrt.akamaized.net/groupa/live/a9f36fda-cb3c-4b4e-9405-a5bba55654c0/live.isml/.m3u8',
        mpeg_dash_128='https://live-radio-cf-vrt.akamaized.net/groupa/live/a9f36fda-cb3c-4b4e-9405-a5bba55654c0/live.isml/.mpd',
        mp3_128='http://icecast.vrtcdn.be/klara-high.mp3',
        mp3_64='http://icecast.vrtcdn.be/klara-mid.mp3',
        aac_128='http://icecast.vrtcdn.be/klara.aac',
        logo='https://radioplayer.vrt.be/iframe/img/channelLogos/klara.png',
        backdrop='https://images.vrt.be/orig/2014/11/19/2cef6c86-6fcb-11e4-aec2-00163edf75b7.jpg',
        epg_id='klara.be',
        preset=903,
    ),
    dict(
        id='32',
        name='klara-continuo',
        label='Klara Continuo',
        tagline='Non-stop klassieke muziek',
        website='https://klara.be/',
        hls_128='https://live-radio-cf-vrt.akamaized.net/groupa/live/0d06dbbe-92d4-4cfe-a0b3-ccc6b7a32ec4/live.isml/.m3u8',
        mpeg_dash_128='https://live-radio-cf-vrt.akamaized.net/groupa/live/0d06dbbe-92d4-4cfe-a0b3-ccc6b7a32ec4/live.isml/.mpd',
        mp3_128='http://icecast.vrtcdn.be/klaracontinuo-high.mp3',
        mp3_64='http://icecast.vrtcdn.be/klaracontinuo-mid.mp3',
        aac_128='http://icecast.vrtcdn.be/klaracontinuo.aac',
        logo='https://radioplayer.vrt.be/iframe/img/channelLogos/klaracontinuo.png',
        backdrop='https://images.vrt.be/orig/2014/08/14/cfbe90a7-23b6-11e4-8e74-00163edf75b7.jpg',
        epg_id='klaracontinuo.be',
        preset=929,
    ),
    dict(
        id='41',
        name='stubru',
        label='Studio Brussel',
        tagline='Life is Music',
        website='https://stubru.be/',
        hls_128='https://live-radio-cf-vrt.akamaized.net/groupc/live/f404f0f3-3917-40fd-80b6-a152761072fe/live.isml/.m3u8',
        mpeg_dash_128='https://live-radio-cf-vrt.akamaized.net/groupc/live/f404f0f3-3917-40fd-80b6-a152761072fe/live.isml/.mpd',
        mp3_128='http://icecast.vrtcdn.be/stubru-high.mp3',
        mp3_64='http://icecast.vrtcdn.be/stubru-mid.mp3',
        aac_128='http://icecast.vrtcdn.be/stubru.aac',
        logo='https://radioplayer.vrt.be/iframe/img/channelLogos/stubru.png',
        backdrop='https://images.vrt.be/orig/2014/08/14/8e1aa87c-23b2-11e4-8e74-00163edf75b7.jpg',
        epg_id='stubru.be',
        preset=904,
    ),
    dict(
        id='44',
        name='stubru-tijdloze',
        label='StuBru De Tijdloze',
        tagline='Altijd en overal de beste Tijdloze muziek',
        website='https://stubru.be/',
        hls_128='https://live-radio-cf-vrt.akamaized.net/groupc/live/582109ca-1e71-4330-93fc-e9affee94d7d/live.isml/.m3u8',
        mpeg_dash_128='https://live-radio-cf-vrt.akamaized.net/groupc/live/582109ca-1e71-4330-93fc-e9affee94d7d/live.isml/.mpd',
        mp3_128='http://icecast.vrtcdn.be/stubru_tijdloze-high.mp3',
        mp3_64='http://icecast.vrtcdn.be/stubru_tijdloze-mid.mp3',
        aac_128='http://icecast.vrtcdn.be/stubru_tijdloze.aac',
        logo='https://radioplayer.vrt.be/iframe/img/channelLogos/detijdloze.png',
        backdrop='https://images.vrt.be/orig/2014/08/14/8e1aa87c-23b2-11e4-8e74-00163edf75b7.jpg',
        epg_id='stubrutijdloze.be',
        preset=930,
    ),
    dict(
        id='45',
        name='stubru-tgs',
        label='StuBru #ikluisterbelgisch',
        tagline='Non-Stop. Nieuw. Belgisch.',
        website='https://stubru.be/',
        hls_128='https://live-radio-cf-vrt.akamaized.net/groupc/live/23384e71-2b6a-43f1-8ad6-02c4ebb8bdf7/live.isml/.m3u8',
        mpeg_dash_128='https://live-radio-cf-vrt.akamaized.net/groupc/live/23384e71-2b6a-43f1-8ad6-02c4ebb8bdf7/live.isml/.mpd',
        mp3_128='http://icecast.vrtcdn.be/stubru_tgs-high.mp3',
        mp3_64='http://icecast.vrtcdn.be/stubru_tgs-mid.mp3',
        aac_128='http://icecast.vrtcdn.be/stubru_tgs.aac',
        logo='https://radioplayer.vrt.be/iframe/img/channelLogos/ikluisterbelgisch.png',
        backdrop='https://images.vrt.be/orig/2014/08/14/8e1aa87c-23b2-11e4-8e74-00163edf75b7.jpg',
        epg_id='stubruikluisterbelgisch.be',
        preset=931,
    ),
    dict(
        id='141',
        name='stubru-bruut',
        label='StuBru Bruut',
        tagline='Alleen maar stevige gitaren',
        website='https://stubru.be/',
        hls_128='https://live-radio-vrt.akamaized.net/groupc/live/556a688c-d0b6-4969-9a01-747e4e4944bb/live.isml/.m3u8',
        mpeg_dash_128='https://live-radio-vrt.akamaized.net/groupc/live/556a688c-d0b6-4969-9a01-747e4e4944bb/live.isml/.mpd',
        mp3_128='http://icecast.vrtcdn.be/stubru_bruut-high.mp3',
        mp3_64='http://icecast.vrtcdn.be/stubru_bruut-mid.mp3',
        aac_128='http://icecast.vrtcdn.be/stubru_bruut.aac',
        logo='https://radioplayer.vrt.be/iframe/img/channelLogos/bruut.png',
        backdrop='https://images.vrt.be/orig/2014/08/14/8e1aa87c-23b2-11e4-8e74-00163edf75b7.jpg',
        epg_id='stubrubruut.be',
        preset=932,
    ),
    dict(
        id='140',
        name='stubru-hooray',
        label='StuBru Hooray',
        tagline='Non-stop hiphop',
        website='https://stubru.be/',
        hls_128='https://live-radio-vrt.akamaized.net/groupc/live/5024acc8-180a-4c50-b05f-0f32f2aba0ea/live.isml/.m3u8',
        mpeg_dash_128='https://live-radio-vrt.akamaized.net/groupc/live/5024acc8-180a-4c50-b05f-0f32f2aba0ea/live.isml/.mpd',
        mp3_128='http://icecast.vrtcdn.be/stubru_hiphophooray-high.mp3',
        mp3_64='http://icecast.vrtcdn.be/stubru_hiphophooray-mid.mp3',
        aac_128='http://icecast.vrtcdn.be/stubru_hiphophooray.aac',
        logo='https://radioplayer.vrt.be/iframe/img/channelLogos/hooray.png',
        backdrop='https://images.vrt.be/orig/2014/08/14/8e1aa87c-23b2-11e4-8e74-00163edf75b7.jpg',
        epg_id='stubruhooray.be',
        preset=933,
    ),
    dict(
        id='142',
        name='stubru-untz',
        label='StuBru Untz',
        tagline='The party never stops',
        website='https://stubru.be/',
        hls_128='https://live-radio-cf-vrt.akamaized.net/groupb/live/90cb8bb1-1ed0-40d3-bbad-47690a2a5fc3/live.isml/.m3u8',
        mpeg_dash_128='https://live-radio-cf-vrt.akamaized.net/groupb/live/90cb8bb1-1ed0-40d3-bbad-47690a2a5fc3/live.isml/.mpd',
        mp3_128='http://icecast.vrtcdn.be/stubru_untz-high.mp3',
        mp3_64='http://icecast.vrtcdn.be/stubru_untz-mid.mp3',
        aac_128='http://icecast.vrtcdn.be/stubru_untz.aac',
        logo='https://radioplayer.vrt.be/iframe/img/channelLogos/bruut.png',
        backdrop='https://images.vrt.be/orig/2014/08/14/8e1aa87c-23b2-11e4-8e74-00163edf75b7.jpg',
        epg_id='stubruuntz.be',
        preset=934,
    ),
    dict(
        id='55',
        name='mnm',
        label='MNM',
        tagline='Music and More',
        website='https://mnm.be/',
        hls_128='https://live-radio-cf-vrt.akamaized.net/groupa/live/68dc3b80-040e-4a75-a394-72f3bb7aff9a/live.isml/.m3u8',
        mpeg_dash_128='https://live-radio-cf-vrt.akamaized.net/groupa/live/68dc3b80-040e-4a75-a394-72f3bb7aff9a/live.isml/.mpd',
        mp3_128='http://icecast.vrtcdn.be/mnm-high.mp3',
        mp3_64='http://icecast.vrtcdn.be/mnm-mid.mp3',
        aac_128='http://icecast.vrtcdn.be/mnm.aac',
        logo='https://radioplayer.vrt.be/iframe/img/channelLogos/mnm.png',
        backdrop='https://images.vrt.be/orig/2014/08/13/b662a3a3-22da-11e4-8e74-00163edf75b7.png',
        epg_id='mnm.be',
        preset=905,
    ),
    dict(
        id='56',
        name='mnm-hits',
        label='MNM Hits',
        tagline='Music and More - The Hits',
        website='https://mnm.be/',
        hls_128='https://live-radio-cf-vrt.akamaized.net/groupb/live/35dd91de-0352-4865-8632-17e5af8dc6ba/live.isml/.m3u8',
        mpeg_dash_128='https://live-radio-cf-vrt.akamaized.net/groupb/live/35dd91de-0352-4865-8632-17e5af8dc6ba/live.isml/.mpd',
        mp3_128='http://icecast.vrtcdn.be/mnm_hits-high.mp3',
        mp3_64='http://icecast.vrtcdn.be/mnm_hits-mid.mp3',
        aac_128='http://icecast.vrtcdn.be/mnm_hits.aac',
        logo='https://radioplayer.vrt.be/iframe/img/channelLogos/mnmhits.png',
        backdrop='https://images.vrt.be/orig/2014/08/13/c4a7e1e7-22e1-11e4-8e74-00163edf75b7.png',
        epg_id='mnmhits.be',
        preset=940,
    ),
    dict(
        id='57',
        name='mnm-juice',
        label='MNM Juice',
        tagline='De online stream met de beste juicy vibes van MNM',
        website='https://mnm.be/',
        hls_128='https://live-radio-cf-vrt.akamaized.net/groupa/live/da0b681c-73db-4c9e-af32-7921591d3fbd/live.isml/.m3u8',
        mpeg_dash_128='https://live-radio-cf-vrt.akamaized.net/groupa/live/da0b681c-73db-4c9e-af32-7921591d3fbd/live.isml/.mpd',
        mp3_128='http://icecast.vrtcdn.be/mnm_urb-high.mp3',
        mp3_64='http://icecast.vrtcdn.be/mnm_urb-mid.mp3',
        aac_128='http://icecast.vrtcdn.be/mnm_urb.aac',
        logo='https://radioplayer.vrt.be/iframe/img/channelLogos/mnmjuice.png',
        backdrop='https://images.vrt.be/orig/2014/08/13/c4a7e1e7-22e1-11e4-8e74-00163edf75b7.png',
        epg_id='mnmjuice.be',
        preset=941,
    ),
    dict(
        id='58',
        name='mnm-90s00s',
        label="MNM Back to the 90's & nillies",
        tagline='Music and More',
        website='https://mnm.be/',
        hls_128='https://live-radio-cf-vrt.akamaized.net/groupc/live/a2050115-96cb-4151-afda-cbd177407e6e/live.isml/.m3u8',
        mpeg_dash_128='https://live-radio-cf-vrt.akamaized.net/groupc/live/a2050115-96cb-4151-afda-cbd177407e6e/live.isml/.mpd',
        mp3_128='http://icecast.vrtcdn.be/mnm_90s00s-high.mp3',
        mp3_64='http://icecast.vrtcdn.be/mnm_90s00s-mid.mp3',
        aac_128='http://icecast.vrtcdn.be/mnm_90s00s.aac',
        logo='https://radioplayer.vrt.be/iframe/img/channelLogos/mnm90s00s.png',
        backdrop='https://images.vrt.be/orig/2014/08/13/c4a7e1e7-22e1-11e4-8e74-00163edf75b7.png',
        epg_id='mnmbacktothe90snillies.be',
        preset=942,
    ),
    dict(
        id='13',
        name='vrtnws',
        label='VRT Nieuws',
        tagline='Ieder moment het meest recente nieuws',
        website='https://www.vrtnieuws.be/',
        hls_128='https://ondemand-radio-cf-vrt.akamaized.net/audioonly/content/fixed/11_11niws-snip_hi.mp4/.m3u8',
        mpeg_dash_128='https://ondemand-radio-cf-vrt.akamaized.net/audioonly/content/fixed/11_11niws-snip_hi.mp4/.mpd',
        mp3_128='https://progressive-audio.lwc.vrtcdn.be/content/fixed/11_11niws-snip_hi.mp3',
        logo='https://radioplayer.vrt.be/iframe/img/channelLogos/vrtnws.png',
        backdrop='https://images.vrt.be/orig/2014/08/14/0ad165f8-23b7-11e4-8e74-00163edf75b7.jpg',
        epg_id='vrtnws.be',
        preset=950,
    ),
    dict(
        id='03',
        name='ketnet-hits',
        label='Ketnet Hits',
        tagline='De hipste, de coolste én de plezantste hits op een rijtje!',
        website='https://ketnet.be/',
        hls_128='https://live-radio-cf-vrt.akamaized.net/groupa/live/014a9eea-af85-4da6-aab2-c472ca8d0149/live.isml/.m3u8',
        mpeg_dash_128='https://live-radio-cf-vrt.akamaized.net/groupa/live/014a9eea-af85-4da6-aab2-c472ca8d0149/live.isml/.mpd',
        mp3_128='http://icecast.vrtcdn.be/ketnetradio-high.mp3',
        mp3_64='http://icecast.vrtcdn.be/ketnetradio-mid.mp3',
        aac_128='http://icecast.vrtcdn.be/ketnetradio.aac',
        logo='https://radioplayer.vrt.be/iframe/img/channelLogos/ketnethits.png',
        backdrop='https://images.vrt.be/orig/2015/06/18/ea4ace5e-1586-11e5-8223-00163edf48dd.jpg',
        epg_id='ketnethits.be',
        preset=944,
    ),
    dict(
        id='71',
        name='vrt-event',
        label='VRT Event',
        tagline='',
        website='https://vrt.be/',
        hls_128='https://live-radio-cf-vrt.akamaized.net/groupa/live/779d53fc-9472-4fe8-b62a-1d38c5878c60/live.isml/.m3u8',
        mpeg_dash_128='https://live-radio-cf-vrt.akamaized.net/groupa/live/779d53fc-9472-4fe8-b62a-1d38c5878c60/live.isml/.mpd',
        mp3_128='http://icecast.vrtcdn.be/vrtevent-high.mp3',
        mp3_64='http://icecast.vrtcdn.be/vrtevent-mid.mp3',
        aac_128='http://icecast.vrtcdn.be/vrtevent.aac',
        logo='https://radioplayer.vrt.be/iframe/img/channelLogos/vrtnws.png',
        backdrop='https://images.vrt.be/orig/2014/08/14/0ad165f8-23b7-11e4-8e74-00163edf75b7.jpg',
        epg_id='vrtevent.be',
        preset=951,
    ),
    dict(
        id='21',
        name='radio2-antwerpen',
        label='Radio 2 (Antwerpen)',
        tagline='De grootste familie',
        website='https://radio2.be/',
        hls_128='https://live-radio-cf-vrt.akamaized.net/groupb/live/033d312d-31f7-400a-b81a-61195f0b79c5/live.isml/.m3u8',
        mpeg_dash_128='https://live-radio-cf-vrt.akamaized.net/groupb/live/033d312d-31f7-400a-b81a-61195f0b79c5/live.isml/.mpd',
        mp3_128='http://icecast.vrtcdn.be/ra2ant-high.mp3',
        mp3_64='http://icecast.vrtcdn.be/ra2ant-mid.mp3',
        aac_128='http://icecast.vrtcdn.be/ra2ant.aac',
        logo='https://radioplayer.vrt.be/iframe/img/channelLogos/radio2ant.png',
        backdrop='https://images.vrt.be/orig/2014/10/29/3a06a4e4-5f6f-11e4-aec2-00163edf75b7.jpg',
        epg_id='radio2ant.be',
        preset=925,
    ),
    dict(
        id='23',
        name='radio2-limburg',
        label='Radio 2 (Limburg)',
        tagline='De grootste familie',
        website='https://radio2.be/',
        hls_128='https://live-radio-cf-vrt.akamaized.net/groupb/live/d9c49923-b49f-4ab3-8532-4e9bd850b4e2/live.isml/.m3u8',
        mpeg_dash_128='https://live-radio-cf-vrt.akamaized.net/groupb/live/d9c49923-b49f-4ab3-8532-4e9bd850b4e2/live.isml/.mpd',
        mp3_128='http://icecast.vrtcdn.be/ra2lim-high.mp3',
        mp3_64='http://icecast.vrtcdn.be/ra2lim-mid.mp3',
        aac_128='http://icecast.vrtcdn.be/ra2lim.aac',
        logo='https://radioplayer.vrt.be/iframe/img/channelLogos/radio2lim.png',
        backdrop='https://images.vrt.be/orig/2014/10/29/3a06a4e4-5f6f-11e4-aec2-00163edf75b7.jpg',
        epg_id='radio2lim.be',
        preset=926,
    ),
    dict(
        id='24',
        name='radio2-oost-vlaanderen',
        label='Radio 2 (Oost-Vlaanderen)',
        tagline='De grootste familie',
        website='https://radio2.be/',
        hls_128='https://live-radio-cf-vrt.akamaized.net/groupb/live/93a8a402-9008-4a97-b473-bc107be7524d/live.isml/.m3u8',
        mpeg_dash_128='https://live-radio-cf-vrt.akamaized.net/groupb/live/93a8a402-9008-4a97-b473-bc107be7524d/live.isml/.mpd',
        mp3_128='http://icecast.vrtcdn.be/ra2ovl-high.mp3',
        mp3_64='http://icecast.vrtcdn.be/ra2ovl-mid.mp3',
        aac_128='http://icecast.vrtcdn.be/ra2ovl.aac',
        logo='https://radioplayer.vrt.be/iframe/img/channelLogos/radio2ovl.png',
        backdrop='https://images.vrt.be/orig/2014/10/29/3a06a4e4-5f6f-11e4-aec2-00163edf75b7.jpg',
        epg_id='radio2ovl.be',
        preset=927,
    ),
    dict(
        id='25',
        name='radio2-west-vlaanderen',
        label='Radio 2 (West-Vlaanderen)',
        tagline='De grootste familie',
        website='https://radio2.be/',
        hls_128='https://live-radio-cf-vrt.akamaized.net/groupc/live/604e4a0e-22e8-4f99-ad5e-4f62d27dfec4/live.isml/.m3u8',
        mpeg_dash_128='https://live-radio-cf-vrt.akamaized.net/groupc/live/604e4a0e-22e8-4f99-ad5e-4f62d27dfec4/live.isml/.mpd',
        mp3_128='http://icecast.vrtcdn.be/ra2wvl-high.mp3',
        mp3_64='http://icecast.vrtcdn.be/ra2wvl-mid.mp3',
        aac_128='http://icecast.vrtcdn.be/ra2wvl.aac',
        logo='https://radioplayer.vrt.be/iframe/img/channelLogos/radio2wvl.png',
        backdrop='https://images.vrt.be/orig/2014/10/29/3a06a4e4-5f6f-11e4-aec2-00163edf75b7.jpg',
        epg_id='radio2wvl.be',
        preset=928,
    ),
]