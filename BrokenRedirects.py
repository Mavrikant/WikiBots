# -*- coding: utf-8 -*-
# !/usr/bin/python
from bs4 import BeautifulSoup
import requests
import mavri
import re

xx = mavri.login('tr.wikipedia', 'Mavrikant')
content = requests.get('https://tr.wikipedia.org/wiki/%C3%96zel:BozukY%C3%B6nlendirmeler').text
soup = BeautifulSoup(content, 'html.parser')

for line in soup.find("div", {"id": "mw-content-text"}).ol.find_all('li'):
    page = line.find_all('a')[0].get('title')
    pagetext = requests.get('https://tr.wikipedia.org/w/index.php?title=' + page + '&action=raw').text
    sil = re.findall('\{\{\s?[Ss]il\s?\|?\s?[^\}]*\s?\}\}', pagetext)
    redirect = re.findall('\[\[\s?([^\]]*)\s?\]\]', pagetext)[0]
    redirectpagetext = requests.get('https://tr.wikipedia.org/w/index.php?title=' + redirect + '&action=raw').text

    if pagetext != '' and redirectpagetext == '' and not sil:
        HS = '{{Sil | Y1. Var olmayan sayfalara olan yönlendirmeler silinebilir. --~~~~}}\n\n'
        mavri.change_page('tr.wikipedia', page, HS + pagetext, '+ Hızlı sil, var olmayan sayfaya yönlendirme', xx)
        mavri.appendtext_on_page('tr.wikipedia', 'Kullanıcı:Mavrikant/Log/BrokenRedirects',
                                 '\n* [[' + page + ']] -> [[' + redirect + ']]',
                                 '[[' + page + ']] -> [[' + redirect + ']]', xx)
exit(0)
