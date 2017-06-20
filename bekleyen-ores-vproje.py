# -*- coding: utf-8 -*-
# !/usr/bin/python
import requests
from bs4 import BeautifulSoup
import re
import mavri

wiki = 'tr.wikipedia'
trwiki = 'https://tr.wikipedia.org'
xx = mavri.login(wiki, 'Mavrikant')

results = {
    u"10K": [],
    u"Antarktika": [],
    u"Anime ve Manga": [],
    u"Ankara": [],
    u"Azerbaycan": [],
    u"Balkanlar": [],
    u"Breaking Bad": [],
    u"Bilim": [],
    u"Bilim tarihi": [],
    u"Buffy evreni": [],
    u"Din": [],
    u"Edebiyat": [],
    u"Elektronik sporlar": [],
    u"Eurovision": [],
    u"Fransa": [],
    u"Futbol": [],
    u"GM": [],
    u"Hande Yener": [],
    u"Harry Potter": [],
    u"Hristiyanlık": [],
    u"Hukuk": [],
    u"Kafkasya": [],
    u"Kimya": [],
    u"Kürt sineması": [],
    u"Kıbrıs": [],
    u"LGBT": [],
    u"Lady Gaga": [],
    u"MHB": [],
    u"Madonna": [],
    u"Müzik": [],
    u"Orta Doğu": [],
    u"Osmanlı": [],
    u"Otomobil": [],
    u"Rihanna": [],
    u"Sanat": [],
    u"Sinema": [],
    u"Siyaset": [],
    u"Sovyetler Birliği": [],
    u"Spor": [],
    u"Tarih": [],
    u"Televizyon dizileri": [],
    u"Tenis": [],
    u"Tiyatro": [],
    u"Türkiye": [],
    u"Tıp": [],
    u"Veteriner Tıp": [],
    u"Çin": [],
    u"İnternet": [],
    u"İstanbul": [],
    u"İsviçre": [],
    u"Diğer": []
}
threshold=40


nextpage = '/w/index.php?title=Özel:BekleyenDeğişiklikler&dir=prev&limit=100'
while nextpage != 'DONE':
    soup = BeautifulSoup(requests.get('https://' + wiki + '.org' + nextpage, cookies=xx.cookies).text, 'html.parser')
    try:
        nextpage = soup.findAll("a", {"class": "mw-prevlink"})[0].get('href')
    except:
        nextpage = 'DONE'

    for line in soup.find("div", {"id": "mw-content-text"}).ul.find_all('li'):
        title = line.find_all('a')[0].get('title')
        incele = line.find_all('a')[2].get('href')
        fark = re.findall(ur'bayt">([^<]*)<', str(line))[0]
        talk_page = "Talk:" + title
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

        content = mavri.content_of_section(wiki, talk_page, 0, xx)
        projects = re.findall(ur'\{\{\s*[Vv]ikiProje\s*\|\s*[Pp]roje\s*\=\s*([^\|]*)', content)

        for project in projects:
            try:
                results[project.strip()].append([title, fark, incele])
            except:
                results[u"Diğer"].append([title, fark, incele])

# Report pending change on every project
xx = mavri.login(wiki, 'Mavrikant Bot')
for project in results:
    content = '\'\'\'Güncellenme tarihi:\'\'\' {{subst:CURRENTDAY}} {{subst:CURRENTMONTHNAME}} {{subst:CURRENTYEAR}} {{subst:CURRENTDAYNAME}} {{subst:CURRENTTIME}} (UTC)'
    for page in results[project]:
        content = content + '\n# [[' + page[0] + ']] ({{Geçmiş|' + page[0] + '|geçmiş}}) ' + page[
            1] + ' ([https://tr.wikipedia.org' + page[2] + ' incele])'

    mavri.change_page(wiki, 'User:Mavrikant Bot/Bekleyen/Proje/' + project, content, 'Güncelleme', xx)
exit(0)
