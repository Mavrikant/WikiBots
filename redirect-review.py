# -*- coding: utf-8 -*-
# !/usr/bin/python
import requests
from bs4 import BeautifulSoup
import mavri

xx = mavri.login('tr.wikipedia', 'Mavrikant')

api_page_link = 'https://tr.wikipedia.org/w/api.php?action=query&format=json&utf8&list=unreviewedpages&urnamespace=0&urfilterredir=redirects&urlimit=50&urstart='

nextpage=""
while nextpage != 'DONE':
    api_page=requests.get(api_page_link+nextpage, cookies=xx.cookies)
    try:
        nextpage = api_page.json()['continue']['urstart']
    except:
        nextpage = 'DONE'

    for page in api_page.json()['query']['unreviewedpages']:
        print page['title']
        try:
            diff= requests.get('https://tr.wikipedia.org/w/api.php?action=query&format=json&utf8&prop=revisions&titles='+page['title']+'&rvprop=ids', cookies=xx.cookies).json()['query']['pages'].itervalues().next()['revisions'][0]['revid']
            mavri.review_diff('tr.wikipedia', diff, xx)
            print "DONE"
        except:
            print "ERROR"


exit(0)
