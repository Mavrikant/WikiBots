# -*- coding: utf-8 -*-
# !/usr/bin/python
from bs4 import BeautifulSoup
import requests

import mavri

xx = mavri.login('tr.wikipedia', 'Mavrikant')
content = requests.get(
    'https://tr.wikipedia.org/w/index.php?title=%C3%96zel:BekleyenDe%C4%9Fi%C5%9Fiklikler&dir=prev&limit=100',
    cookies=xx.cookies).text
soup = BeautifulSoup(content, 'html.parser')

RAPOR = '{| class="wikitable"\n|-\n! Sayfa !! Damaging !! Reverted'

for line in soup.find("div", {"id": "mw-content-text"}).ul.find_all('li'):
    incele = line.find_all('a')[2].get('href')
    title = line.find_all('a')[0].get('title')
    incele_text = requests.get('https://tr.wikipedia.org' + incele, cookies=xx.cookies).text

    if incele_text.find('diff-multi') == -1:
        diff = incele_text.split('<input id="mw-fr-input-oldid" type="hidden" value="')[1].split('"')[0]
        print title
        # print diff
        damaging = \
            requests.get('http://ores.wmflabs.org/scores/trwiki/damaging/' + str(diff)).json()[str(diff)][
                'probability'][
                'true'] * 100
        reverted = \
            requests.get('http://ores.wmflabs.org/scores/trwiki/reverted/' + str(diff)).json()[str(diff)][
                'probability'][
                'true'] * 100
        # print damaging
        # print reverted
        RAPOR += '\n|-\n| [https://tr.wikipedia.org' + incele + ' ' + title + '] || ' + str(damaging) + ' || ' + str(
            reverted)

RAPOR += '\n|}'

print mavri.change_page('tr.wikipedia', 'Kullanıcı:Mavrikant/ORES', RAPOR, 'ORES', xx)
exit(0)
