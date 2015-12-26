# -*- coding: utf-8 -*-
import mavri
import requests
from bs4 import BeautifulSoup

xx = mavri.login('tr.wikipedia', 'Mavrikant')
trwiki = 'https://tr.wikipedia.org'

nextpage = '/w/index.php?title=%C3%96zel:BekleyenDe%C4%9Fi%C5%9Fiklikler&limit=100&namespace=&level=-1&size=0'
while nextpage != 'DONE':
    soup = BeautifulSoup(requests.get(trwiki + nextpage).text, 'html.parser')
    try:
        nextpage = soup.findAll("a", {"class": "mw-nextlink"})[0].get('href')
    except:
        nextpage = 'DONE'

    for line in soup.find("div", {"id": "mw-content-text"}).ul.find_all('li'):
        title = line.find_all('a')[2].get('title')
        link = line.find_all('a')[2].get('href')
        FARK = requests.get(trwiki + link, cookies=xx.cookies).text

        if FARK.find('<div class="mw-diff-empty">(Fark yok)</div>') != -1:
            diff = FARK.split('<input id="mw-fr-input-oldid" type="hidden" value="')[1].split('" name="oldid" />')[0]
            RAPOR = '\n* ' + title + ' -  [[Special:Diff/' + str(diff) + ']]\n** '
            RAPOR += mavri.review_diff('tr.wikipedia', diff, xx).text
            mavri.appendtext_on_page('tr.wikipedia', 'Kullanıcı:Mavrikant/Log/FarkYok', RAPOR,
                                     '+Bot ile oto onaylanmış değişilik', xx)
