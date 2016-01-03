# -*- coding: utf-8 -*-
# !/usr/bin/python
from bs4 import BeautifulSoup
import requests

import mavri

xx = mavri.login('tr.wikipedia', 'Mavrikant')
trwiki = 'https://tr.wikipedia.org'
nextpage = '/w/index.php?title=%C3%96zel:BekleyenDe%C4%9Fi%C5%9Fiklikler&limit=100'
while nextpage != 'DONE':
    soup = BeautifulSoup(requests.get(trwiki + nextpage, cookies=xx.cookies).text, 'html.parser')
    try:
        nextpage = soup.findAll("a", {"class": "mw-nextlink"})[0].get('href')
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
            if damaging < 20 or reverted < 20:
                mavri.review_diff('tr.wikipedia', diff, xx)
                mavri.appendtext_on_page('tr.wikipedia', 'Kullanıcı:Mavrikant/ORES/Reviewed',
                                         '\n* [[Special:Diff/' + str(diff) + ' | ' + title + ']]', title, xx)

exit(0)
