# -*- coding: utf-8 -*-
# !/usr/bin/python

from bs4 import BeautifulSoup
import requests
import mavri
import re
import json


def read_param(parameter):
    if parameter in parameters:
        result = parameters[parameter]
        if not result == '':
            result = result[0].upper() + result[1:]
        return result
    else:
        return ''


wiki = 'tr.wikipedia'
xx = mavri.login(wiki, 'Mavrikant Bot')
VikiProje_name = "Tarih"
template = 'Şablon:VikiProje '+VikiProje_name
summary = u"VikiProje "+VikiProje_name+" şablonu standartlaştırma"
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
        try:
            title = page['title']
            ns = page['ns']
            print title
            content = mavri.content_of_section('tr.wikipedia', title, 0, xx)
            # print content
            paramet = re.findall(ur'\{\{\s*[Vv]ikiProje '+VikiProje_name+ur'([^\}]*)\}\}', content)[0].split("|")
            parameters = {}
            for para in paramet:
                if "=" in para:
                    parameters[para.split("=")[0].strip()] = para.split("=")[1].strip()
                    
            replacement = "{{VikiProje |Proje = " + VikiProje_name + " |Sınıf = " + read_param(
                u'sınıf') + " |Önem = " + read_param(u'önem') + " }}"

            content = re.sub(ur'\{\{\s*[Vv]ikiProje '+VikiProje_name+ur'([^\}]*)\}\}', replacement, content)
            content = re.sub(ur'\{\{\s*[Tt]artışma\s*\}\}\n?', '', content)
            content = '{{Tartışma}}\n' + content
            content = re.sub(ur'\}\}\s*\n+\s*\{\{', '}}\n{{', content)
            
            if ns is 1: #Tartışma sayfası ile YİB konktrolü yap
                entity = mavri.wikibase_item(wiki, title.split(':')[1])
                if (mavri.wbgetclaims(entity, 'P570').text == '{"claims":{}}') and (
                            '"id":"Q5"' in mavri.wbgetclaims(entity, 'P31').text):
                    content = re.sub(ur'\{\{\s*[Yy][İi][Bb]\s*\}\}\n?', '', content)
                    content = '{{YİB}}\n' + content

            # print "======="
            # print content
            mavri.change_section(wiki, title, 0, content, summary, xx)
        except:
            print "error"
