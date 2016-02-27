# -*- coding: utf-8 -*-
# !/usr/bin/python

import requests

import mavri

wiki = 'tr.wikipedia'
xx = mavri.login(wiki, 'Mavrikant')
user = '71.191.3.59'
usercontribs = requests.get(
    'https://tr.wikipedia.org/w/api.php?action=query&list=usercontribs&format=json&uclimit=500&ucuser=' + user,
    cookies=xx.cookies)

for cont in usercontribs.json()['query']['usercontribs']:
    diff = cont['revid']
    print mavri.review_diff('tr.wikipedia', diff, xx).text
