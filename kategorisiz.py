# -*- coding: utf-8 -*-
# !/usr/bin/python

import re

import requests
from bs4 import BeautifulSoup

import mavri

wiki = 'tr.wikipedia'
wikiS = 'trwiki'
xx = mavri.login(wiki, 'Mavrikant Bot')
catNS = requests.get(
        'https://' + wiki + '.org/w/api.php?format=json&utf8=&action=query&meta=siteinfo&siprop=namespaces').json()[
    'query']['namespaces']['14']['*']


def add_category(page):
    print page
    if mavri.content_of_page(wiki, page):
        ENpage = mavri.wbgetlanglink(mavri.wikibase_item(wiki, page), 'enwiki')
        if ENpage:
            print ENpage
            ENcat = mavri.categories_on_enwiki(ENpage)
            print ENcat
            cat_to_add = []
            for cat in ENcat:
                ncat = mavri.wbgetlanglink(mavri.wikibase_item('en.wikipedia', 'Category:' + cat), wikiS)
                if ncat != '':
                    cat_to_add.insert(0, ncat)
            print cat_to_add
            content = mavri.content_of_page(wiki, page)
            appendtext = ''
            for cat in cat_to_add:
                if re.findall(r'\[\[\s?' + cat + '\s?\|?[^\[\]]*\]\]', content) == []:
                    appendtext += '\n[[' + cat + ']]'

            NUM = str(len(cat_to_add))
            if appendtext:
                content += appendtext
                content = re.sub(r'\{\{\s?[Kk]ategorisiz[^\}]*\}\}\s?\n?', '', content)
                content = re.sub(r'\{\{\s?[Uu]ncategorized[^\}]*\}\}\s?\n?', '', content)
                diff = mavri.change_page(wiki, page, content, '++' + NUM + catNS, xx).json()['edit']['newrevid']
                mavri.appendtext_on_page(wiki, 'Kullanıcı:Mavrikant_Bot/Log/Kategorisiz',
                                         '\n# [[Special:Diff/' + str(diff) + '|' + page + ']] (+' + NUM + ' Kategori)',
                                         '[[Special:Diff/' + str(diff) + '|' + page + ']] (' + NUM + ' Kategori)', xx)
            else:
                content = mavri.content_of_page(wiki, page)
                if re.findall(r'\[\[\s?' + catNS + '[^\]]*\]\]', content) == [] and re.findall(
                        r'\{\{\s?[Kk]ategorisiz[^\}]*\}\}', content) == []:
                    content = re.sub(r'\{\{\s?[Kk]ategorisiz[^\}]*\}\}\s?\n?', '', content)
                    content = re.sub(r'\{\{\s?[Uu]ncategorized[^\}]*\}\}\s?\n?', '', content)
                    diff = mavri.change_page(wiki, page,
                                             content + '\n\n{{Kategorisiz|{{kopyala:CURRENTMONTHNAME}} {{kopyala:CURRENTYEAR}}}} ',
                                             '++Kategorisiz Şablonu', xx).json()['edit']['newrevid']
                    mavri.appendtext_on_page(wiki, 'Kullanıcı:Mavrikant_Bot/Log/Kategorisiz',
                                             '\n# [[Special:Diff/' + str(diff) + '|' + page + ']] (Kategorisiz)',
                                             '[[Special:Diff/' + str(diff) + '|' + page + ']] (Kategorisiz)', xx)
        else:
            content = mavri.content_of_page(wiki, page)
            if re.findall(r'\[\[\s?' + catNS + '[^\]]*\]\]', content) == [] and re.findall(
                    r'\{\{\s?[Kk]ategorisiz[^\}]*\}\}', content) == []:
                content = re.sub(r'\{\{\s?[Kk]ategorisiz[^\}]*\}\}\s?\n?', '', content)
                content = re.sub(r'\{\{\s?[Uu]ncategorized[^\}]*\}\}\s?\n?', '', content)
                diff = mavri.change_page(wiki, page,
                                         content + '\n\n{{Kategorisiz|{{kopyala:CURRENTMONTHNAME}} {{kopyala:CURRENTYEAR}}}} ',
                                         '++Kategorisiz Şablonu', xx).json()['edit']['newrevid']
                mavri.appendtext_on_page(wiki, 'Kullanıcı:Mavrikant_Bot/Log/Kategorisiz',
                                         '\n# [[Special:Diff/' + str(diff) + '|' + page + ']] (Kategorisiz)',
                                         '[[Special:Diff/' + str(diff) + '|' + page + ']] (Kategorisiz)', xx)


# Section 1
cats = mavri.pages_on_category(wiki, 'Kategori:Kategorisiz')
for line in cats:
    page = line['title']
    add_category(page)

# Section 2
content = requests.get('https://' + wiki + '.org/w/index.php?title=Special:UncategorizedPages&limit=500&offset=0').text
datelog = 'Kullanıcı:Mavrikant_Bot/Log/Kategorisiz/Tarih'
olddate = mavri.content_of_page(wiki, datelog)
newdate = content.split('son güncelleme zamanı: ')[1].split('.')[0]

if olddate != newdate:
    mavri.change_page(wiki, datelog, newdate, newdate, xx)
    soup = BeautifulSoup(content, 'html.parser')
    for line in soup.find("div", {"id": "mw-content-text"}).ol.find_all('li'):
        page = line.find_all('a')[0].get('title')
        add_category(page)
