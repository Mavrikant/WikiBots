# -*- coding: utf-8 -*-
# !/usr/bin/python
import requests
from bs4 import BeautifulSoup

import mavri

xx = mavri.login('tr.wikipedia', 'Mavrikant')
trwiki = 'https://tr.wikipedia.org'

nextpage = '/w/index.php?title=Özel:BekleyenDeğişiklikler&dir=prev&limit=50'
while nextpage != 'DONE':
    soup = BeautifulSoup(requests.get(trwiki + nextpage, cookies=xx.cookies).text, 'html.parser')
    try:
        nextpage = soup.findAll("a", {"class": "mw-prevlink"})[0].get('href')
    except:
        nextpage = 'DONE'

    for line in soup.find("div", {"id": "mw-content-text"}).ul.find_all('li'):
        incele = line.find_all('a')[2].get('href')
        title = line.find_all('a')[0].get('title')

        incele_text = requests.get(trwiki + incele, cookies=xx.cookies).text

        if incele_text.find('diff-multi') == -1:
            diff = incele_text.split('<input id="mw-fr-input-oldid" type="hidden" value="')[1].split('"')[0]

            damaging = \
                requests.get('http://ores.wmflabs.org/scores/trwiki/damaging/' + str(diff)).json()[str(diff)][
                    'probability'][
                    'true'] * 100
            reverted = \
                requests.get('http://ores.wmflabs.org/scores/trwiki/reverted/' + str(diff)).json()[str(diff)][
                    'probability'][
                    'true'] * 100
            print title + ': ' + str(damaging) + ' ' + str(reverted)
            if damaging < 25 and reverted < 25:
                print '#onayla'
                mavri.review_diff('tr.wikipedia', diff, xx)
                text = '[[Special:Diff/' + str(diff) + ' | ' + title + ']] - damaging= %.2f - reverted= %.2f' %(damaging, reverted)
                mavri.appendtext_on_page('tr.wikipedia', 'Kullanıcı:Mavrikant/ORES/Reviewed', '\n# ' + text, text, xx)
exit(0)
