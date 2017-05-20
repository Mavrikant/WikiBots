# -*- coding: utf-8 -*-
# !/usr/bin/python
import requests
from bs4 import BeautifulSoup
import re
import mavri

xx = mavri.login('tr.wikipedia', 'Mavrikant Bot')
wiki='tr.wikipedia'

nextpage = '.org/w/index.php?title=Özel:BekleyenDeğişiklikler&dir=prev&limit=50'
while nextpage != 'DONE':
    soup = BeautifulSoup(requests.get('https://'+wiki + nextpage, cookies=xx.cookies).text, 'html.parser')
    try:
        nextpage = soup.findAll("a", {"class": "mw-prevlink"})[0].get('href')
    except:
        nextpage = 'DONE'

    for line in soup.find("div", {"id": "mw-content-text"}).ul.find_all('li'):
        title = line.find_all('a')[0].get('title')
        talk_page="Talk:"+title

        content=mavri.content_of_section(wiki, talk_page, 0, xx)
        projects = re.findall(ur'\{\{\s*[Vv]ikiProje\s*\|\s*[Pp]roje\s*\=\s*([^\|]*)', content)
        print projects

exit(0)
