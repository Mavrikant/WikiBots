# -*- coding: utf-8 -*-
# !/usr/bin/python

import re

import mavri

wiki = 'tr.wikipedia'
xx = mavri.login(wiki, 'Mavrikant Bot')

Templates = ['Düzenle', 'Kaynaksız']

for temp in Templates:
    pages = mavri.embeddedin(wiki, 'Şablon:' + temp)
    for page in pages:
        title = page['title']
        content = str(mavri.content_of_page(wiki, title))
        date = re.findall('\{\{\s*' + temp + '\s*\|([^\}]*)\}\}', content, flags=re.IGNORECASE)
        print '*'
        if not date:
            mavri.appendtext_on_page(wiki, 'Kullanıcı:Mavrikant/Log', '\n* ' + temp + ': [[' + title + ']]', '+1', xx)


            # result=requests.get('https://tr.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&titles='+title+'&utf8=1&rvprop=timestamp%7Ccontent&rvlimit=100')
            # for revision in result.json()['query']['pages'].itervalues().next()['revisions']:
            #     print revision['timestamp']
            #
            #     if not revision['*'].find('{{düzenle}}'):
            #         print 'ok'
