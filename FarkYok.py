# -*- coding: utf-8 -*-

import mavri
import requests
from bs4 import BeautifulSoup

xx = mavri.login('tr.wikipedia', 'Mavrikant')
# print xx.text
trwiki = 'https://tr.wikipedia.org'

nextpage = '/w/index.php?title=%C3%96zel:BekleyenDe%C4%9Fi%C5%9Fiklikler&limit=100&namespace=&level=-1&size=0'
while nextpage != 'DONE':
    soup = BeautifulSoup(requests.get(trwiki + nextpage).text, 'html.parser')
    try:
        nextpage = soup.findAll("a", {"class": "mw-nextlink"})[0].get('href')
    except:
        nextpage = 'DONE'
    # print nextpage

    for line in soup.find("div", {"id": "mw-content-text"}).ul.find_all('li'):
        title = line.find_all('a')[2].get('title')
        link = line.find_all('a')[2].get('href')
        print title
        # print link
        FARK = requests.get(trwiki + link, cookies=xx.cookies).text
        # print FARK
        if FARK.find('<div class="mw-diff-empty">(Fark yok)</div>') != -1:
            diff = FARK.split('<input id="mw-fr-input-oldid" type="hidden" value="')[1].split('" name="oldid" />')[0]
            print title
            print diff
            print mavri.review_diff('tr.wikipedia', diff, xx).text
