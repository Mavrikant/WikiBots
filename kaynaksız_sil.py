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
		content = mavri.content_of_section(wiki,title,0,xx)
		content = re.sub(ur'\{\{\s?[Kk]aynaksız[^\}]*\}\}\s?\n?', '', content)

		params3 = '?format=json&action=tokens'
	    	r3 = requests.get('https://' + wiki + '.org/w/api.php' + params3, cookies=xx.cookies)
	    	edit_token = r3.json()['tokens']['edittoken']
	    	edit_cookie = xx.cookies.copy()
	    	edit_cookie.update(r3.cookies)


	    	payload = {'action': 'edit', 'assert': 'user', 'format': 'json', 'utf8': '', 'section': str(0), 'text': content, 'summary': '-Kaynaksız şablonu, '+str(kaynak_sayisi)+' adet kaynak var', 'title': title, 'token': edit_token, 'bot': ''}
	   	requests.post('https://' + wiki + '.org/w/api.php', data=payload, cookies=edit_cookie)		

exit(0)



