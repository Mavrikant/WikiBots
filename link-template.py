# -*- coding: utf-8 -*-

import mavri
import requests
from bs4 import BeautifulSoup
import re

xx = mavri.login('tr.wikipedia', 'Mavrikant Bot')

while 1:
    soup = BeautifulSoup(requests.get(
        'https://tr.wikipedia.org/w/index.php?title=%C3%96zel:Ba%C4%9FArama&limit=500&offset=0&target=http%3A%2F%2Fwww.mackolik.com%2FFutbolcu',
        cookies=xx.cookies).text, 'html.parser')

    for line in soup.find("ol", {"class": "special"}).find_all('li'):
        title = line.find_all('a')[1].get('title')
        print title
        content = mavri.content_of_page('tr.wikipedia', title)
        content = re.sub(r'\[\s?http://www.mackolik.com/Futbolcu/(\d*)[^\]]*\]', r'{{Mackolik.com futbolcu|\1}}',
                         content)

        mavri.change_page('tr.wikipedia', title, content, 'mackolik.com linkleri şablona dönüştürüldü', xx)
