# -*- coding: utf-8 -*-
# !/usr/bin/python

import mavri
import datetime
from random import randint

wiki = 'tr.wikipedia'
xx = mavri.login(wiki, 'Mavrikant Bot')

one_day = datetime.timedelta(days=1)
now = datetime.datetime.now()
ilk = datetime.date(2015, 9, 1)
bugun = datetime.date(now.year, now.month, now.day)
yarin = bugun + one_day + one_day
kaynak = ilk + randint(0, int(str(bugun - ilk).split(' days')[0])) * one_day

Log_page = 'Kullanıcı:Mavrikant Bot/Log/Günün Maddesi'


if (yarin.strftime("%d") == '01'):  # Yeni ay temizliği
    mavri.page_clear(wiki, Log_page, 'Yeni ay temizliği', xx)

YARIN = mavri.content_of_page(wiki, 'Şablon:GM/' + yarin.strftime("%Y-%m-%d"))

if (YARIN == ''):  # yarın boş
    Summary = 'Olumsuz'
    Durum = '\n* {{Çapraz}}'

    # Kaynak söz bul ve al
    KAYNAK = ''
    while KAYNAK == '':
        KAYNAK = mavri.content_of_page(wiki, 'Şablon:GM/' + kaynak.strftime("%Y-%m-%d"))
        kaynak += one_day

    # Kaynak söz ile yarını oluştur
    mavri.change_page(wiki, 'Şablon:GM/' + yarin.strftime("%Y-%m-%d"), KAYNAK,
                       '[[Şablon:GM/' + kaynak.strftime("%Y-%m-%d") + ']] sayfasından kopyalandı.', xx)

else:  # yarın dolu
    Summary = 'Olumlu'
    Durum = '\n* {{Tamam}}'

Durum += ' [[Şablon:GM/' + yarin.strftime("%Y-%m-%d") + ' | \'\'\'' + yarin.strftime("%d.%m.%Y") + '\'\'\']]'

mavri.sent_message(wiki, Log_page, Durum, Summary+' (WMF-Labs)', xx)