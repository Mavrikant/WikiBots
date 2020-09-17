# -*- coding: utf-8 -*-
# !/usr/bin/python

# mavri kütüphanesi yükle
import mavri

# json kütüphanesi yükle
import json

wiki='tr.wikipedia'
username= 'Mavrikant Bot'

# Kullanıcı girişi yap
xx = mavri.login(wiki, username)

# Giriş denemesini sonucunu ekrana JSON ile düzenleyerek yazdır
print json.dumps(json.loads(xx.text), sort_keys=True, indent=4)

# 2 bölümü birbirinden ayır
print "\n-------------------------------------------------------------------------\n" 

# Deneme sayfasına mesaj ekle. 
sonuc = mavri.appendtext_on_page('tr.wikipedia', 'Vikipedi:Deneme tahtası', '\n== mavribot test ==\nDeneme deneme 123 --~~~~', 'mavribot ile test yapıldı.', xx)

# Sonucu ekrana JSON ile düzenleyerek yazdır
print json.dumps(json.loads(sonuc.text), sort_keys=True, indent=4)

# Programı kapat
exit(0)
