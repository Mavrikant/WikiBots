# -*- coding: utf-8 -*-
# !/usr/bin/python
from bs4 import BeautifulSoup
import requests
import mavri
import re

xx= mavri.login('www.wikidata','Mavrikant')

wiki='https://tr.wikipedia.org'
template='Şablon:TFF futbolcu'
value= r'\{\{TFF futbolcu\|(\d*)\}\}'
property= 'P2448'

ticontinue = ''
while ticontinue != 'DONE':
    allpages= requests.get(wiki+'/w/api.php?action=query&utf8&format=json&tiprop=title&titles='+template+'&prop=transcludedin&tilimit=500&ticontinue='+str(ticontinue))
    try:
        ticontinue =allpages.json()['continue']['ticontinue']
    except:
        ticontinue = 'DONE'

    for page in allpages.json()['query']['pages'].itervalues().next()['transcludedin']:

        title = page['title']
        print title
        content = mavri.content_of_page('tr.wikipedia',title)
        if re.findall(value, content)[0]:
            id = re.findall(value, content)[0]
            entity= mavri.wikibase_item('tr.wikipedia',title)

            if  mavri.wbgetclaims(entity, property).text == '{"claims":{}}':
                print mavri.wbcreateclaim(entity,property,'value', str(id), xx).text

exit(0)