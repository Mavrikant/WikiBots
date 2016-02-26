# -*- coding: utf-8 -*-
# !/usr/bin/python

import re

import requests

import mavri

wiki = 'tr.wikipedia'
xx = mavri.login(wiki, 'Mavrikant')
months = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık']
Templates = ['Düzenle', 'Kaynaksız', 'Temizleme', 'Viki-bağlantısız', 'Çıkmaz sokak']

for temp in Templates:
    pages = mavri.embeddedin(wiki, 'Şablon:' + temp)
    for page in pages:
        title = page['title']
        print temp + ': ' + title
        content = str(mavri.content_of_page(wiki, title))
        date = re.findall('\{\{\s*' + temp + '\s*\|([^\}]*)\}\}', content, flags=re.IGNORECASE)
        if not date:
            revisions = requests.get(
                    'https://tr.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&titles=' + title + '&utf8=1&rvprop=ids|timestamp|content&rvlimit=1000')
            for revision in revisions.json()['query']['pages'].itervalues().next()['revisions']:
                if not re.search('\{\{\s*' + temp + '\s*\}\}', str(revision['*']), re.IGNORECASE):
                    break
                timestamp = revision['timestamp']
                diff = revision['revid']
            year = timestamp[:4]
            month = months[int(timestamp[5:7]) - 1]
            text = re.sub('\{\{\s*' + temp + '\s*\}\}', '{{' + temp + '|' + month + ' ' + year + '}}', content,
                          flags=re.I)
            summary = temp + ' şablonuna tarih eklendi. [[Special:Diff/' + str(diff) + '|Kaynak]]'
            mavri.change_page(wiki, title, text, summary, xx)
