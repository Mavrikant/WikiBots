# -*- coding: utf-8 -*-
# !/usr/bin/python
import requests
from bs4 import BeautifulSoup
import re
import mavri

wiki='tr.wikipedia'
xx = mavri.login(wiki, 'Mavrikant Bot')

results = {
u"10K": [],
u"Antarktika": [],
u"Anime ve Manga": [],
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

nextpage = '/w/index.php?title=Özel:BekleyenDeğişiklikler&dir=prev&limit=100'
while nextpage != 'DONE':
    soup = BeautifulSoup(requests.get('https://'+wiki +'.org'+ nextpage, cookies=xx.cookies).text, 'html.parser')
    try:
        nextpage = soup.findAll("a", {"class": "mw-prevlink"})[0].get('href')
    except:
        nextpage = 'DONE'

    for line in soup.find("div", {"id": "mw-content-text"}).ul.find_all('li'):
        title = line.find_all('a')[0].get('title')
        incele = line.find_all('a')[2].get('href')
        fark = re.findall(ur'bayt">([^<]*)<',str(line))
        talk_page="Talk:"+title

        content = mavri.content_of_section(wiki, talk_page, 0, xx)
        projects = re.findall(ur'\{\{\s*[Vv]ikiProje\s*\|\s*[Pp]roje\s*\=\s*([^\|]*)', content)

        for project in projects:
            try:
                results[project.strip()].append([title, fark, incele])
            except:
                results[u"Diğer"].append([title, fark, incele])


for project in results:
    content='\'\'\'Güncellenme tarihi:\'\'\' {{subst:CURRENTDAY}} {{subst:CURRENTMONTHNAME}} {{subst:CURRENTYEAR}} {{subst:CURRENTDAYNAME}} {{subst:CURRENTTIME}} (UTC)'
    for page in results[project]:
        content=content+'\n# [['+page[0]+']] ({{Geçmiş|'+page[0]+'|geçmiş}}) '+page[1]+' ([https://tr.wikipedia.org'+ page[2]+' incele])'
    
    mavri.change_page(wiki, 'User:Mavrikant Bot/Bekleyen/Proje/'+project, content, 'Güncelleme', xx)
exit(0)
