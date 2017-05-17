# -*- coding: utf-8 -*-

import time
import requests
import mavri

wiki='tr.wikipedia'
xx = mavri.login(wiki, 'Mavrikant Bot')

baseurl = u'https://tr.wikipedia.org/w/'
title = u'Kullanıcı:Mavrikant_Bot/Bekleyen'
title2=u'Şablon:BEKLEYENSAYISI'
page = u'https://tr.wikipedia.org/wiki/Özel:Doğrulamaİstatistikleri'
oldtimee = u'empty'

while 1:
    r1 = requests.get(page)
    r1 = r1.text.split(u'Aşağıdaki veriler, en son ')[1]
    timee = r1.split(u' tarihinde güncellenmiştir.')[0]

    number = r1.split(
        u'<a href="/w/index.php?title=%C3%96zel:BekleyenDe%C4%9Fi%C5%9Fiklikler&amp;namespace=0" title="Özel:BekleyenDeğişiklikler">')[
        1]
    number = number.split(u'</a></td>')[0]
    bekleyentext = number + ' - ' + timee

    if (oldtimee != timee):
        oldtimee = timee
        appendtext = '\n* ' + bekleyentext + ' (UTC)\n'
        summary = bekleyentext + ' (WMF Labs)'
        mavri.appendtext_on_page(wiki, title, appendtext, summary, xx):
        mavri.change_page(wiki, title2, number, summary, xx):        


    time.sleep(60 * 10)
