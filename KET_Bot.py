# -*- coding: utf-8 -*-
# !/usr/bin/python

import re
import time

import mavri

wiki = 'tr.wikipedia'
xx = mavri.login(wiki, 'KET Bot')
title = 'Vikipedi:Kullanıcı engelleme talepleri'
version = 'V2.1'
summary_ek = " (WMF-Labs, " + version + ")"
section = 1

while 1:

    content = mavri.content_of_section(wiki, title, section, xx)

    if content != '':
        vandal = re.findall('\{\{\s*[Vv]andal\s*\|\s*([^\}]*)\s*\}\}', content)

        if vandal:
            timestamp = re.findall('\{\{\s*KET Bot\s*\|\s*([^\|\}]*)\s*\|\s*[^\|\}]*\s*\}\}', content)[0]
            informer = re.findall('\{\{\s*KET Bot\s*\|\s*[^\|\}]*\s*\|\s*([^\|\}]*)\s*\}\}', content)[0]
            vandal = vandal[0]
            blocked = mavri.blocked(wiki, vandal)
            if blocked.json()['query']['blocks']:
                by = blocked.json()['query']['blocks'][0]['by']
                reason = blocked.json()['query']['blocks'][0]['reason']
                summary = '[[Özel:Katkılar/' + vandal + '|' + vandal + ']] çıkartıldı. [[Kullanıcı:' + by + '|' + by + ']] - ' + reason + summary_ek
                mavri.section_clear(wiki, title, section, summary, xx)
                message = '\n*Merhaba. [[Özel:Katkılar/' + vandal + '|' + vandal + ']], [[Kullanıcı mesaj:' + by + '|' + by + ']] tarafından engellendi. Engel açıklaması:' + reason + ' Bildirimde bulunduğunuz için teşekkürler --~~~~'
                summary = '[[Özel:Katkılar/' + vandal + '|' + vandal + ']], [[Kullanıcı mesaj:' + by + '|' + by + ']] tarafından engellendi.' + summary_ek
                mavri.sent_message(wiki, 'Kullanıcı mesaj:' + informer, message, summary, xx)
        else:
            print mavri.section_clear(wiki, title, section, '{{Vandal|XXXX}} içermeyen başlık kaldırıldı.' + summary_ek, xx).text
        section += 1
    else:
        section = 1
        time.sleep(60)
