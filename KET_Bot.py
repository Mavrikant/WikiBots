# -*- coding: utf-8 -*-
# !/usr/bin/python

import re
import socket
import time
from datetime import datetime

import mavri

wiki = 'tr.wikipedia'
xx = mavri.login(wiki, 'KET Bot')
title = 'Vikipedi:Kullanıcı engelleme talepleri'
version = 'V2.3'
summary_ek = " (WMF-Labs, " + version + ")"
section = 1
ignore_list=[]
mpa = dict.fromkeys(range(32))

while 1:
    content = mavri.content_of_section(wiki, title, section, xx)

    if content != '':
        vandal = re.findall('\{\{\s*[Vv]andal\s*\|\s*([^\}]*)\s*\}\}', content)

        if vandal:
            timestamp = re.findall('\{\{\s*KET Bot\s*\|\s*([^\|\}]*)\s*\|\s*[^\|\}]*\s*\}\}', content)[0]
            informer = re.findall('\{\{\s*KET Bot\s*\|\s*[^\|\}]*\s*\|\s*([^\|\}]*)\s*\}\}', content)[0]
            vandal = vandal[0]
            blocked = mavri.blocked(wiki, vandal)
            not_time = datetime(int(timestamp[:4]), int(timestamp[4:6]), int(timestamp[6:8]), int(timestamp[8:10]),
                                int(timestamp[10:12]), int(timestamp[12:14]))
            vandal = vandal.translate(mpa)

            try:
                socket.inet_aton(vandal)
                IP = 1
            except socket.error:
                IP = 0

            if blocked.json()['query']['blocks']:
                timestamp = blocked.json()['query']['blocks'][0]['timestamp']
                blocked_time = datetime(int(timestamp[:4]), int(timestamp[5:7]), int(timestamp[8:10]),
                                        int(timestamp[11:13]), int(timestamp[14:16]), int(timestamp[17:19]))
                elapsed_time = str(blocked_time - not_time).replace('days,', 'gün')
                by = blocked.json()['query']['blocks'][0]['by']
                reason = blocked.json()['query']['blocks'][0]['reason']

                summary = '[[Özel:Katkılar/' + vandal + '|' + vandal + ']] engellenmiş. [[Kullanıcı:' + by + '|' + by + ']] - ' + reason + summary_ek
                mavri.section_clear(wiki, title, section, summary, xx)


                ignore_page=mavri.content_of_page('tr.wikipedia', 'Kullanıcı:KET_Bot/Yoksay')
                ignore_list= re.split('\s*\*\s*', ignore_page)
                if informer not in ignore_list:
                    message = '\n\n== KET Bot Bildirim ==\nMerhaba. [[Özel:Katkılar/' + vandal + '|' + vandal + ']], siz bildirim yaptıktan ' + elapsed_time + ' saat sonra [[Kullanıcı mesaj:' + by + '|' + by + ']] tarafından engellendi. Engel açıklaması:' + reason + ' Bildirimde bulunduğunuz için teşekkürler. --~~~~'
                    summary = '[[Özel:Katkılar/' + vandal + '|' + vandal + ']], [[Kullanıcı mesaj:' + by + '|' + by + ']] tarafından engellendi.' + summary_ek
                    mavri.sent_message(wiki, 'Kullanıcı mesaj:' + informer, message, summary, xx)
                    
            else:
                now = datetime.now()
                diff = now - not_time

                if IP and diff.total_seconds() > 60 * 60 * 24:
                    summary = '[[Özel:Katkılar/' + vandal + '|' + vandal + ']] çıkartıldı. Bildirim zaman aşımına uğradı.' + summary_ek
                    mavri.section_clear(wiki, title, section, summary, xx)

                    
                    ignore_page=mavri.content_of_page('tr.wikipedia', 'Kullanıcı:KET_Bot/Yoksay')
                    ignore_list= re.split('\s*\*\s*', ignore_page)
                    if informer not in ignore_list:
                        message = '\n\n== KET Bot Bildirim ==\nMerhaba. [[Özel:Katkılar/' + vandal + '|' + vandal + ']], siz bildirim yaptıktan sonra 24 saat geçmesine rağmen engellenmediği için sayfadan çıkartıldı. Bildirimde bulunduğunuz için teşekkürler. --~~~~'
                        summary = '[[Özel:Katkılar/' + vandal + '|' + vandal + ']] bildirimi zaman aşımına uğradı.' + summary_ek
                        mavri.sent_message(wiki, 'Kullanıcı mesaj:' + informer, message, summary, xx)
                if IP == 0 and diff.total_seconds() > 60 * 60 * 24 * 5:
                    summary = '[[Özel:Katkılar/' + vandal + '|' + vandal + ']] çıkartıldı. Bildirim zaman aşımına uğradı.' + summary_ek
                    mavri.section_clear(wiki, title, section, summary, xx)
                    
                    ignore_page=mavri.content_of_page('tr.wikipedia', 'Kullanıcı:KET_Bot/Yoksay')
                    ignore_list= re.split('\s*\*\s*', ignore_page)
                    if informer not in ignore_list:
                        message = '\n\n== KET Bot Bildirim ==\nMerhaba. [[Özel:Katkılar/' + vandal + '|' + vandal + ']], siz bildirim yaptıktan sonra 5 gün geçmesine rağmen engellenmediği için sayfadan çıkartıldı. Bildirimde bulunduğunuz için teşekkürler. --~~~~'
                        summary = '[[Özel:Katkılar/' + vandal + '|' + vandal + ']] bildirimi zaman aşımına uğradı.' + summary_ek
                        mavri.sent_message(wiki, 'Kullanıcı mesaj:' + informer, message, summary, xx)
        else:
            mavri.section_clear(wiki, title, section, '{{Vandal|XXXX}} içermeyen başlık temizlendi.' + summary_ek, xx)
        section += 1
    else:
        section = 1
        time.sleep(60*2)
