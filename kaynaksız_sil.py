# -*- coding: utf-8 -*-
# !/usr/bin/python

from bs4 import BeautifulSoup
import requests
import mavri
import re
import random


xx= mavri.login('tr.wikipedia','Mavrikant Bot')

wiki='tr.wikipedia'
template='Şablon:Kaynaksız'

ticontinue = ''
while ticontinue != 'DONE':
    allpages= requests.get('https://' + wiki + '.org/w/api.php?action=query&utf8&format=json&tiprop=title&titles='+template+'&prop=transcludedin&tilimit=500&ticontinue='+str(ticontinue))
    try:
        ticontinue =allpages.json()['continue']['ticontinue']
    except:
        ticontinue = 'DONE'

    for page in allpages.json()['query']['pages'].itervalues().next()['transcludedin']:

        title = page['title']
	#print title

	content = mavri.content_of_page(wiki, title)
	kaynak_sayisi= len(re.findall(ur'\<\s?\/\s?ref\s?\>', content)) #</ref> 
	print kaynak_sayisi 
	if (kaynak_sayisi>0):
		print title  
		content = mavri.content_of_page(wiki, title)
		content = re.sub(ur'\{\{\s?[Kk]aynaksız[^\}]*\}\}\s?\n?', '', content)
		summary = '-Kaynaksız şablonu, '+str(kaynak_sayisi)+' adet kaynak var'
		mavri.change_page(wiki, title, content, summary, xx)
exit(0)



