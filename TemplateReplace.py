# -*- coding: utf-8 -*-
# !/usr/bin/python

from bs4 import BeautifulSoup
import requests
import mavri
import re
import json


def read_param(parameter):
    if parameter in parameters:
        result = parameters[parameter].capitalize()
        if result is ('Sm' or 'Sl' or 'Km'):
            result = result.upper()
        return result
    else:
        return ''


wiki = 'tr.wikipedia'
xx = mavri.login(wiki, 'Mavrikant Bot')
template = 'Şablon:VikiProje spor'
VikiProje_name = "Spor"
summary = u"VikiProje şablonu standartlaştırma"
ticontinue = ''
while ticontinue != 'DONE':
    allpages = requests.get(
        'https://' + wiki + '.org/w/api.php?action=query&utf8&format=json&tiprop=title&titles=' + template + '&prop=transcludedin&tilimit=5&ticontinue=' + str(
            ticontinue))
    try:
        ticontinue = allpages.json()['continue']['ticontinue']
    except:
        ticontinue = 'DONE'

    for page in allpages.json()['query']['pages'].itervalues().next()['transcludedin']:
        title = page['title']
        ns = page['ns']
        print title
        content = mavri.content_of_section('tr.wikipedia', title, 0, xx)
        # print content
        paramet = re.findall(ur'\{\{\s*[Vv]ikiProje [Ss]por([^\}]*)\}\}', content)[0].split("|")
        parameters = {}
        for para in paramet:
            if "=" in para:
                parameters[para.split("=")[0]] = para.split("=")[1]

        replacement = "{{VikiProje |Proje = " + VikiProje_name + " |Sınıf = " + read_param(
            u'sınıf') + " |Önem = " + read_param(u'önem') + " }}"

        content = re.sub(ur'\{\{\s*[Vv]ikiProje [Ss]por([^\}]*)\}\}', replacement, content)
        content = re.sub(ur'\{\{\s*[Tt]artışma\s*\}\}\n?', '', content)
        content = '{{Tartışma}}\n' + content
        if ns is 1:
            entity = mavri.wikibase_item(wiki, title.split(':')[1])
            if (mavri.wbgetclaims(entity, 'P570').text == '{"claims":{}}') and (
                        '"id":"Q5"' in mavri.wbgetclaims(entity, 'P31').text):
                content = re.sub(ur'\{\{\s*[Yy][İi][Bb]\s*\}\}\n?', '', content)
                content = '{{YİB}}\n' + content

        # print "======="
        # print content
        mavri.change_section(wiki, title, 0, content, summary, xx)
