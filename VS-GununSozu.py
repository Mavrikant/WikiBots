# -*- coding: utf-8 -*-
# !/usr/bin/python

import datetime
from random import randint

import mavri

wiki = 'tr.wikiquote'
xx = mavri.login(wiki, 'Mavrikant Bot')

one_day = datetime.timedelta(days=1)
now = datetime.datetime.now()
ilk = datetime.date(2011, 4, 1)
bugun = datetime.date(now.year, now.month, now.day)
yarin = bugun + one_day
kaynak = ilk + randint(0, int(str(bugun - ilk).split(' days')[0])) * one_day

Log_page = 'Kullanıcı:Mavrikant Bot/Log/Günün Sözü'

if (yarin.strftime("%d") == '01'):  # Yeni ay temizliği
    mavri.page_clear(wiki, Log_page, 'Yeni ay temizliği', xx)

YARIN = mavri.content_of_page(wiki, 'Vikisöz:Günün sözü/' + yarin.strftime("%Y/%m/%d"))

if (YARIN == '' or YARIN.find('Wikimedia Error') != -1):  # yarın boş
    Summary = 'Olumsuz'
    Durum = '\n* {{Çapraz}}'

    # Kaynak söz bul ve al
    KAYNAK = mavri.content_of_page(wiki, 'Vikisöz:Günün sözü/' + kaynak.strftime("%Y/%m/%d"))
    while KAYNAK == '':
        kaynak += one_day
        KAYNAK = mavri.content_of_page(wiki, 'Vikisöz:Günün sözü/' + kaynak.strftime("%Y/%m/%d"))

    # Kaynak söz ile yarını oluştur
    mavri.change_page(wiki, 'Vikisöz:Günün sözü/' + yarin.strftime("%Y/%m/%d"), KAYNAK,
                      '[[Vikisöz:Günün sözü/' + kaynak.strftime("%Y/%m/%d") + ']] sayfasından kopyalandı.', xx)

else:  # yarın dolu
    Summary = 'Olumlu'
    Durum = '\n* {{Tamam}}'

Durum += ' [[Vikisöz:Günün sözü/' + yarin.strftime("%Y/%m/%d") + ' | \'\'\'' + yarin.strftime("%d.%m.%Y") + '\'\'\']]'

mavri.sent_message(wiki, Log_page, Durum, Summary + ' (WMF-Labs)', xx)
