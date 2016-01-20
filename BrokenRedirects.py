# -*- coding: utf-8 -*-
# !/usr/bin/python
import re

import requests
from bs4 import BeautifulSoup

import mavri

wiki = 'tr.wikipedia'
xx = mavri.login(wiki, 'Mavrikant')
content = requests.get('https://tr.wikipedia.org/wiki/%C3%96zel:BozukY%C3%B6nlendirmeler').text
soup = BeautifulSoup(content, 'html.parser')

for line in soup.find("div", {"id": "mw-content-text"}).ol.find_all('li'):
    page = line.find_all('a')[0].get('title')
    print page
    pagetext = mavri.content_of_page(wiki, page)
    print pagetext
    if pagetext != '':
        sil = re.findall('\{\{\s?[Ss]il[^\}]*\}\}', pagetext)
        print sil
        redirect = re.findall('\[\[\s?([^\]]*)\s?\]\]', pagetext)
        print redirect
        if redirect:
            redirectpagetext = mavri.content_of_page(wiki, redirect[0])
            print redirectpagetext
            if redirectpagetext == '' and not sil:
                HS = '{{Sil | Y1. Var olmayan sayfalara olan yönlendirmeler silinebilir. --~~~~}}\n\n'
                mavri.change_page('tr.wikipedia', page, HS + pagetext, '+ Hızlı sil, var olmayan sayfaya yönlendirme',
                                  xx)
                mavri.appendtext_on_page('tr.wikipedia', 'Kullanıcı:Mavrikant/Log/BrokenRedirects',
                                         '\n* [[' + page + ']] -> [[' + redirect[0] + ']]',
                                         '[[' + page + ']] -> [[' + redirect[0] + ']]', xx)

exit(0)
