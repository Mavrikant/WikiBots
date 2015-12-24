# -*- coding: utf-8 -*-

import mavri
import time
import requests

xx = mavri.login('tr.wikipedia', 'Mavrikant Bot')

baseurl = 'https://tr.wikipedia.org/w/'
title = 'Kullanıcı:Mavrikant_Bot/Bekleyen'
page = 'https://tr.wikipedia.org/wiki/%C3%96zel:Do%C4%9Frulama%C4%B0statistikleri'
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

        # get edit token2
        params3 = '?format=json&action=tokens'
        r3 = requests.get(baseurl + 'api.php' + params3, cookies=xx.cookies)
        edit_token = r3.json()['tokens']['edittoken']

        edit_cookie = xx.cookies.copy()
        edit_cookie.update(r3.cookies)

        # save action
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        payload = {'action': 'edit', 'assert': 'user', 'format': 'json', 'utf8': '',
                   'appendtext': '\n* ' + bekleyentext + ' (UTC)\n', 'summary': bekleyentext + ' (WMF Labs)',
                   'title': title, 'token': edit_token, 'bot': ''}
        r4 = requests.post(baseurl + 'api.php', headers=headers, data=payload, cookies=edit_cookie)

    time.sleep(60 * 30)
