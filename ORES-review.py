# -*- coding: utf-8 -*-
# !/usr/bin/python
import requests
from bs4 import BeautifulSoup
import re
import mavri

xx = mavri.login('tr.wikipedia', 'Mavrikant')
trwiki = 'https://tr.wikipedia.org'
threshold=40

nextpage = '/w/index.php?title=Özel:BekleyenDeğişiklikler&dir=prev&limit=50'
while nextpage != 'DONE':
    soup = BeautifulSoup(requests.get(trwiki + nextpage, cookies=xx.cookies).text, 'html.parser')
    try:
        nextpage = soup.findAll("a", {"class": "mw-prevlink"})[0].get('href')
    except:
        nextpage = 'DONE'

    for line in soup.find("div", {"id": "mw-content-text"}).ul.find_all('li'):
        incele = line.find_all('a')[2].get('href')
        title = line.find_all('a')[0].get('title')
        incele_text = requests.get(trwiki + incele, cookies=xx.cookies).text

        content = requests.get(trwiki+'/w/index.php?title='+title+'&action=history', cookies=xx.cookies).text
        diff_ids = re.findall(ur'diff=(\d*)">inceleme bekliyor</a>', content)
        for diff in reversed(diff_ids):
            damaging = requests.get('http://ores.wmflabs.org/scores/trwiki/damaging/' + str(diff)).json()[str(diff)]['probability']['true'] * 100
            reverted = requests.get('http://ores.wmflabs.org/scores/trwiki/reverted/' + str(diff)).json()[str(diff)]['probability']['true'] * 100
            log = '[[Special:Diff/' + str(diff) + ' | ' + title + ']] - damaging= %.2f - reverted= %.2f' % (damaging, reverted)
            print log
            if damaging < threshold and reverted < threshold:
                mavri.review_diff('tr.wikipedia', diff, xx)
                mavri.appendtext_on_page('tr.wikipedia', 'Kullanıcı:Mavrikant/ORES/Reviewed', '\n# ' + log, log, xx)
            else:
                break

exit(0)
