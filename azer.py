# -*- coding: utf-8 -*-
# !/usr/bin/python

import mavri
import requests

wiki = 'tr.wikipedia'
xx = mavri.login(wiki, 'Mavrikant')

allpages ="""Tartışma:Zira FK
Tartışma:Ziliban, Zakatala
Tartışma:Zengilan
Tartışma:Zengele, Yardımlı
Tartışma:Zeynelezir, Yardımlı
Tartışma:Nesibe Zeynalova
Tartışma:Zevin, Yardımlı
Tartışma:Hasanbey Zerdabi
Tartışma:Zerdab
Tartışma:Zakatala Şehir Stadyumu
Tartışma:Zakatala
Tartışma:Lütfi Zade
Tartışma:Aziza Mustafa Zadeh
Tartışma:Zabrat Stadyumu
Tartışma:Yukarı Eskipara
Tartışma:Yukarı Astanlı, Yardımlı
Tartışma:Sami Yusuf
Tartışma:Namık Yusifov
Tartışma:Nesib Bey Yusufbeyli
Tartışma:Elvin Yunuszade
Tartışma:Yuhu
Tartışma:Yolocak, Yardımlı
Tartışma:Yevlah Stadyumu
Tartışma:Yevlah Havalimanı
Tartışma:Yevlah
Tartışma:Yergüc,Kuba
Tartışma:Yeniyol
Tartışma:Yenice
Tartışma:Yeni Abdinli, Yardımlı
Tartışma:Yaşar Nuri (oyuncu)
Tartışma:Yaşar Mehmetzade Stadyumu
Tartışma:Yasamal
Tartışma:Yarımca
Tartışma:Yardımlı
Tartışma:Xoşkeşin
Tartışma:Hatai, Bakü
Tartışma:Xəzər TV
Tartışma:Kanbulak, Yardımlı
Tartışma:Bütün Azerbaycan Halk Cephesi Partisi
Tartışma:When the Music Dies
Tartışma:Batı Üniversitesi
Tartışma:Güneybatı Asya
Tartışma:Biz Dağlarımızız
Tartışma:Azerbaycan vatandaşlarının tabi olduğu vize uygulamaları
Tartışma:Azerbaycan'ın vize politikası
Tartışma:Verov, Yardımlı
Tartışma:Vergedüz, Yardımlı
Tartışma:Velikanlı, Yardımlı
Tartışma:Mir Hasan Vezirov
Tartışma:Van Papurisi
Tartışma:Vagif Anıt mezarı
Tartışma:Uzundere (dans)
Tartışma:Urakeran, Yardımlı
Tartışma:Unformal
Tartışma:2020 Avrupa Futbol Şampiyonası
Tartışma:Udinler
Tartışma:Ucar
Tartışma:Türkiye İşçi ve Çiftçi Sosyalist Fırkası
Tartışma:Türk Keneşi
Tartışma:Turan Tovuz İK
Tartışma:Sahurlar
Tartışma:Türkmençay Antlaşması
Tartışma:Ferhat Paşa Antlaşması
Tartışma:Behmen Mirze Hazinesi
Tartışma:Azerbaycan'da ulaşım
Tartışma:Transkafkasya Demokratik Federatif Cumhuriyeti
Tartışma:Güney Kafkasya
Tartışma:Trans Anadolu doğalgaz boru hattı
Tartışma:Bakü tramvay hattı
Tartışma:Gatarın demiryol stansiyasına dahil olması
Tartışma:Alimerdan Topçubaşov
Tartışma:Tevfik İsmailov Stadyumu
Tartışma:Tevfik Behramov Stadyumu
Tartışma:Tilekend, Yardımlı
Tartışma:Üçüncü Göktürk-Sasani Savaşı
Tartışma:Üçüncü Eurovision Dans Yarışması
Tartışma:Azerbaycan tiyatrosu
Tartışma:Balahanıda neft fontanı
Tartışma:Bibiheybetde neft fontanı yanğını
Tartışma:Gafgaz regsi
Tartışma:Tazekend, Yardımlı
Tartışma:Teyvaz
Tartışma:Aysel Teymurzade
Tartışma:Teşkan, Yardımlı
Tartışma:Azerbaycan'da televizyon
Tartışma:Rabita Bakü
Tartışma:Televar, Yardımlı
Tartışma:Tatarlı
Tartışma:Tatlar
Tartışma:Tatça
Tartışma:Terter
Tartışma:Terekeme (halk oyunu)
Tartışma:Tar (çalgı)
Tartışma:Tamzara
Tartışma:Talış-Mugan Özerk Cumhuriyeti
Tartışma:Talışlar
Tartışma:Talışça
Tartışma:Talış Hanlığı
Tartışma:Nigar Talibova
Tartışma:I. Tahmasb
Tartışma:Tahire Tahirova
Tartışma:Tahirli, Yardımlı
Tartışma:Zeynelabidin Tağıyev
Tartışma:Tefekkür Üniversitesi
Tartışma:Şurud
Tartışma:Surahanı
Tartışma:Sumgayıt FK
Tartışma:Ayna Sultanova
Tartışma:Şahin Sultanov
Tartışma:Azerbaycan Sınır Koruma Kuvvetleri
Tartışma:Mariya Stadnik
Tartışma:Space TV
Tartışma:Şovut, Yardımlı
Tartışma:Lorenzo Sotomayor
Tartışma:Richard Sorge
Tartışma:Solgard, Yardımlı
Tartışma:SOCAR Tower
Tartışma:SOCAR
Tartışma:Şıhlar, Yardımlı
Tartışma:Şıhhüseynli, Yardımlı
Tartışma:Sırık, Yardımlı
Tartışma:Sepasdia Bar
Tartışma:Şin, Şeki
Tartışma:Simurg PİK
Tartışma:Şilevenge, Yardımlı
Tartışma:Şuşa
Tartışma:Şirvanşah
Tartışma:Şirvan Hanlığı
Tartışma:Şirvan (Azerbaycan)
Tartışma:Aliağa Şıhlinski
Tartışma:Şiilik
Tartışma:Şerif Şerifov
Tartışma:Şamlı (etnik grup)
Tartışma:Şemkir FK
Tartışma:Şemkir Şehir Stadyumu
Tartışma:Şeki Hanlığı
Tartışma:Stepan Şaumyan
Tartışma:Şaumyan
Tartışma:Şahsevenler
Tartışma:Şahdağ halkları
Tartışma:Şah
Tartışma:Şemkir
Tartışma:Şele, Yardımlı
Tartışma:Şeher bağında halg gezintisi
Tartışma:Şefikli, Yardımlı
Tartışma:Sederek
Tartışma:Züleyha Seyidmemmedova
Tartışma:Yahyâ-yı Şirvânî
Tartışma:Yedi Güzel (bale)
Tartışma:Eylül Günleri
Tartışma:Separadi, Yardımlı
Tartışma:Selçuklular
Tartışma:Hazar Üniversitesi Eğitim Fakültesi
Tartışma:Sarı Gelin
Tartışma:Hüseynkulu Sarabski
Tartışma:Samurçay
Tartışma:Şamlı
Tartışma:Semeni
Tartışma:Salyan
Tartışma:Saltaq
Tartışma:Müsâfirîler
Tartışma:Tahir Salahov
Tartışma:Bakü Surp Krikor Lusavoriç Kilisesi
Tartışma:Şahbuz
Tartışma:Safevî Devleti
Tartışma:Safevî-Kızılbaş tarihi
Tartışma:Necmettin Sadıkov
Tartışma:Sadıkcan
Tartışma:Sabuncu, Bakü
Tartışma:Sabirabad
Tartışma:Bayıl Kalesi
Tartışma:Sebail
Tartışma:Saatlı
Tartışma:Rutullar
Tartışma:Rutulca
Tartışma:Sabir Rüstemhanlı
Tartışma:1826-1828 İran-Rus Savaşı
Tartışma:1804-1813 Rus-İran Savaşı
Tartışma:Mstislav Rostropoviç
Tartışma:Ravan FK
Tartışma:Yuliya Ratkeviç
Tartışma:Artur Rasizade
Tartışma:Vitali Rahimov
Tartışma:Semra Rahimli
Tartışma:Kurudere
Tartışma:Kubadlı
Tartışma:Kuba Hanlığı
Tartışma:Krız
Tartışma:Kobustan
Tartışma:Kıvrak
Tartışma:Kızılbaş
Tartışma:Kazah
Tartışma:Karavuldaş, Yardımlı
Tartışma:Karakoyunlu
Tartışma:Karakaya, Yardımlı
Tartışma:Karapapaklar
Tartışma:Karalı
Tartışma:Karadağ, Bakü
Tartışma:Qaradağ Lökbatan FK
Tartışma:Karabağ FK
Tartışma:Kah
Tartışma:Kaçarlar (halk)
Tartışma:Kafkas Üniversitesi (Azerbaycan)
Tartışma:Kabakdibi, Yardımlı
Tartışma:Kebele
Tartışma:Azerbaycan resmî tatil günleri
Tartışma:Haçın Melikliği
Tartışma:Porsova, Yardımlı
Tartışma:Perimbel, Yardımlı
Tartışma:Peşteser, Yardımlı
Tartışma:Farslar
Tartışma:Fars edebiyatı
Tartışma:Farsça
Tartışma:Ernani Pereira
Tartışma:Pax Khazarica
Tartışma:Yıldırımlı Yollarla (bale)
Tartışma:Allahşükür Paşazade
Tartışma:Ganire Paşayeva
Tartışma:Niyameddin Paşayev
Tartışma:Paşalı
Tartışma:Ümit Partisi (Azerbaycan)
Tartışma:Azerbaycan Demokratik Islahatlar Partisi
Tartışma:Part İmparatorluğu
Tartışma:Park Bulvar
Tartışma:Papak
Tartışma:Türkçülük
Tartışma:Şeki Hanları Sarayı
Tartışma:Ostayır, Yardımlı
Tartışma:Osnekeran, Yardımlı
Tartışma:Sevinç Osmankızı
Tartışma:Rüstem Orucov
Tartışma:Oruçlu
Tartışma:Karadeniz Ekonomik İşbirliği
Tartışma:Ordubad (anlam ayrımı)
Tartışma:Azerbaycan Operası
Tartışma:İçeri Şehir
Tartışma:Azerice (İran dili)
Tartışma:Ökü, Yardımlı
Tartışma:Odurakeran, Yardımlı
Tartışma:Nevruz
Tartışma:Kuzeydoğu Kafkas dilleri
Tartışma:Nizami, Bakü
Tartışma:Azerbaycan Edebiyatı Müzesi
Tartışma:Nizami Anıt mezarı
Tartışma:Niyazi
Tartışma:Nisegele, Yardımlı
Tartışma:9. Ordu (Osmanlı)
Tartışma:Nesimi, Bakü
Tartışma:Nesimî (anlam ayrımı)
Tartışma:Nerimanov, Bakü
Tartışma:Samuh
Tartışma:Nizami Gencevi
Tartışma:Yeni Azerbaycan Partisi
Tartışma:Neftçala FK
Tartışma:Petrol Taşları
Tartışma:Yakın Doğu
Tartışma:Azerbaycan Ulusal Tarih Müzesi
Tartışma:Azerbeycan'ın Milli Kahramanı
Tartışma:Devlet Bayrağı Meydanı
Tartışma:Azerbaycan arması
Tartışma:Azerbaycan Millî Meclisi
Tartışma:Azerbaycan Ulusal Güzel Sanatlar Müzesi
Tartışma:İmadeddin Nesimî
Tartışma:Nar Mobile
Tartışma:Nahçıvan Devlet Üniversitesi
Tartışma:Nahçıvan Havalimanı
Tartışma:Nahçıvan Şehir Stadyumu
Tartışma:Karabağ Savaşı
Tartışma:Dağlık Karabağ
Tartışma:Nağara
Tartışma:Naftalan
Tartışma:Azerbaycan müziği
Tartışma:Musalı
Tartışma:Musa, Yardımlı
Tartışma:Muğam
Tartışma:Mugan
Tartışma:Çamur volkanı
Tartışma:Dağ Yahudileri
Tartışma:Malakanlar
Tartışma:Molla Nasreddin (dergi)
Tartışma:MOİK Stadyumu
Tartışma:MOİK
Tartışma:Mirimli, Yardımlı
Tartışma:Mevlüd Miraliyev
Tartışma:Azerbaycan Cumhuriyeti Gençlik ve Spor Bakanlığı
Tartışma:Azerbaycan Cumhuriyeti Millî Güvenlik Bakanlığı
Tartışma:Azerbaycan Cumhuriyeti İçişleri Bakanlığı
Tartışma:Azerbaycan Savunma Sanayi Bakanlığı
Tartışma:Azerbaycan Kültür ve Turizm Bakanlığı
Tartışma:Mingeçevir
Tartışma:Mil-Muğan FK
Tartışma:Sabina Mikina
Tartışma:I. Dünya Savaşı'nda Osmanlı cepheleri
Tartışma:Orta Farsça
Tartışma:Orta Doğu
Tartışma:Melikli, Yardımlı
Tartışma:Meyxana
Tartışma:Ahıska Türkleri
Tartışma:Monte Melkonyan
Tartışma:Irène Mélikoff
Tartışma:Samet bey Mehmandarov
Tartışma:Gülnare Mehmandarova
Tartışma:Zemfira Meftahatdinova
Tartışma:Medeniyyet TV
Tartışma:Mezyedi Hanedanı
Tartışma:Martuni
Tartışma:Nasır Menzuri
Tartışma:Mamulğan, Yardımlı
Tartışma:Şehriyar Memmedyarov
Tartışma:Elmar Memmedyarov
Tartışma:Natalya Mammadova
Tartışma:Ferid Memmedov
Tartışma:Eduard Memmedov
Tartışma:Ağası Memmedov
Tartışma:Elnur Memmedli
Tartışma:Kız Kulesi (Bakü)
Tartışma:Müslüm Magomayev (besteci)
Tartışma:Müslüm Magomayev
Tartışma:Azerbaycan'ın katıldığı savaşlar listesi
Tartışma:Türk devletleri listesi
Tartışma:Azerbaycan'daki süpermarket zincirleri listesi
Tartışma:Kürt devletleri ve hanedanlıkları listesi
Tartışma:İrani Devletler
Tartışma:Azerbaycan Premyer Ligası'nda oynayan yabancı futbolcular listesi
Tartışma:Azerbaycan futbol stadyumları listesi
Tartışma:Olimpiyatlarda Azerbaycan bayrak taşıyıcıları listesi
Tartışma:Azerbaycanca televizyon ve radyo kanalları listesi
Tartışma:Lider TV
Tartışma:Azerbaycan'da LGBT hakları
Tartışma:Lezran, Yardımlı
Tartışma:Ləkətağ
Tartışma:Lezginka
Tartışma:Lerik
Tartışma:Lenkeran Havalimanı
Tartışma:Lev Landau
Tartışma:Sarısu Gölü
Tartışma:Göygöl Gölü
Tartışma:Laçin (anlam ayrımı)
Tartışma:Laçın Koridoru
Tartışma:Kürekçi, Yardımlı
Tartışma:Azerbaycan Kürtleri
Tartışma:Kürdemir
Tartışma:Kür Dili Adası
Tartışma:Köryedi, Yardımlı
Tartışma:Köroğlu (opera, Hacıbeyov)
Tartışma:İnessa Korkmaz
Tartışma:Gregoriy Korganov
Tartışma:Kırna
Tartışma:Hudat
Tartışma:Fetali Han Hoyski
Tartışma:Hocavend
Tartışma:Kınalıklılar
Tartışma:Hınalık dili
Tartışma:Kınalık,Kuba
Tartışma:Mirza Hazar
Tartışma:Hazar Üniversitesi
Tartışma:Hazar, Bakü
Tartışma:Kelle paça
Tartışma:Zeyneb Hanlarova
Tartışma:Zülfiye Hanbabayeva
Tartışma:Azerbaycan hanlıkları
Tartışma:Hanende
Tartışma:Flora Kerimova
Tartışma:Keçili
Tartışma:Keçelekeran, Yardımlı
Tartışma:Kebeloba,Zakatala
Tartışma:Dilara Kazımova
Tartışma:Aygün Kazımova
Tartışma:Garri Kasparov
Tartışma:Kaşatag
Tartışma:Karvan İK
Tartışma:Karşılama oyunları
Tartışma:Karayusuflu
Tartışma:Karadağlılar (Türk)
Tartışma:Kerbelayı Sefihan Karabaği
Tartışma:Karabağ atı
Tartışma:Karakoyunlular
Tartışma:Kengerli
Tartışma:Kelbecer
Tartışma:Movses Kagankatvatsi
Tartışma:Culfa, Azerbaycan
Tartışma:Cücelerim
Tartışma:Jiy, Yardımlı
Tartışma:Cekliler
Tartışma:Cekce
Tartışma:Behbud Han Cevanşir
Tartışma:Samir Cevadzade
Tartışma:Nigar Cemal
Tartışma:Ahmediye Cebrayılov
Tartışma:İstiglal
Tartışma:Eddy Silvestre Pascual Israfilov
Tartışma:İsmayıllı
Tartışma:Hatice İsmailova
Tartışma:İsmet Gayibov Stadyumu
Tartışma:Telman İsmailov
Tartışma:I. İsmail
Tartışma:Kafkas İslam Ordusu
Tartışma:İran'da İslam
Tartışma:Radik İsayev
Tartışma:Azerbaycan'da dinsizlik
Tartışma:Mirza Kadim İrevani
Tartışma:İran halkları
Tartışma:1946 İran krizi
Tartışma:İnter PİK
Tartışma:Şefa Stadyumu
Tartışma:İmişli
Tartışma:İmaret Stadyumu
Tartışma:İlhanlılar
Tartışma:Almas İldırım
Tartışma:Şemseddin İldeniz
Tartışma:İdman Azerbaycan TV
Tartışma:İctimai TV
Tartışma:Mübariz İbrahimov
Tartışma:I. İbrahim (Şirvanşah)
Tartışma:İber-Kafkas dilleri
Tartışma:Elnur Hüseynov
Tartışma:Alikram Hummatov
Tartışma:Hümâyun
Tartışma:Hortlak
Tartışma:Horonu, Yardımlı
Tartışma:Horavar, Yardımlı
Tartışma:Honuba Şıhlar, Yardımlı
Tartışma:Honuba, Yardımlı
Tartışma:Hold Me (Ferid Memmedov şarkısı)
Tartışma:İran'daki Yahudilerin tarihi
Tartışma:Azerbaycan Yahudileri
Tartışma:Hasanlı
Tartışma:Haydarabad, Azerbaycan
Tartışma:Haydar Aliyev Stadyumu
Tartışma:Haydar Aliyev Spor ve Fuar Kompleksi
Tartışma:Haydar Aliyev Uluslararası Havalimanı
Tartışma:Haydar Aliyev Vakfı
Tartışma:Haydar Aliyev Kültür Merkezi
Tartışma:Hereti
Tartışma:Uzun Hasan
Tartışma:Zakir Hasanov
Tartışma:Ferid Hasanov
Tartışma:Haput, Kuba
Tartışma:Hamarkend, Yardımlı
Tartışma:Halay
Tartışma:Hacıkabul
Tartışma:Mehmet Hasan Hacınski
Tartışma:Hacı Çelebi Han
Tartışma:Hadrut
Tartışma:Hacılar (anlam ayrımı)
Tartışma:Gürcüva
Tartışma:Güneşli
Tartışma:Güneyli
Tartışma:Günaz TV
Tartışma:Güneşli petrol platformu yangını
Tartışma:Zümrüd Kuluzade
Tartışma:Tarlan Guliyev
Tartışma:Ramil Guliyev
Tartışma:Elçin Quliyev
Tartışma:Gügevar, Yardımlı
Tartışma:GUAM Demokrasi ve Ekonomik Kalkınma Örgütü
Tartışma:Büyük Nizam Partisi
Tartışma:Göktepe
Tartışma:Göygöl
Tartışma:Göydərə
Tartışma:Goranboy
Tartışma:Kümbet
Tartışma:Nekur, Yardımlı
Tartışma:Fikret Koca
Tartışma:Kobustan Millî Parkı
Tartışma:Gilar, Yardımlı
Tartışma:Gersava, Yardımlı
Tartışma:Gedebey
Tartışma:Gendere, Yardımlı
Tartışma:Hetag Gazyumov
Tartışma:Garvanke, Yardımlı
Tartışma:Eldar Kasımov
Tartışma:Vügar Haşimov
Tartışma:Aliya Garayeva
Tartışma:Kara Karayev
Tartışma:Ferec Karayev
Tartışma:Gence Devlet Üniversitesi
Tartışma:Gence Hanlığı
Tartışma:Gence Havalimanı
Tartışma:Gence Stadyumu
Tartışma:Kabala FK
Tartışma:Kabala Şehir Stadyumu
Tartışma:Fuzûlî
Tartışma:Füzuli
Tartışma:Azerbaycan'ın dış ilişkileri
Tartışma:Alev Kuleleri
Tartışma:Azerbaycan bayrağı
Tartışma:Standard Sumgayıt FK
Tartışma:Muğan PFK
Tartışma:Fındıklıkışlak, Yardımlı
Tartışma:Fındıqlı, Zakatala
Tartışma:Bakı FK
Tartışma:I. Fariburz
Tartışma:Fábio Luís Ramim
Tartışma:Evçedulan, Yardımlı
Tartışma:Ersile, Yardımlı
Tartışma:Ərəzin
Tartışma:Ərəfsə
Tartışma:Engevül, Yardımlı
Tartışma:Elik, Kuba
Tartışma:Əbrəqunus
Tartışma:Eymur, Ağdaş
Tartışma:2012 Eurovision Şarkı Yarışması
Tartışma:Revan Hanlığı
Tartışma:Erikli
Tartışma:Energetik FK
Tartışma:İmparatoriçe Aleksandra Fyodorovna adına Rus-Müslüman Kız Mektebi
Tartışma:Dağlık Karabağ Cumhuriyeti'nde seçimler
Tartışma:İldenizliler
Tartışma:Azerbaycan ekonomisi
Tartışma:Ekonomik İşbirliği Teşkilatı
Tartışma:Şark Ordular Grubu
Tartışma:Dovga
Tartışma:Dizə, Culfa
Tartışma:Diyadin, Şerur
Tartışma:Diana Hacıyeva
Tartışma:Deryavar, Yardımlı
Tartışma:Dellekli, Yardımlı
Tartışma:Derbent Hanlığı
Tartışma:Deman, Yardımlı
Tartışma:İstiklâl Beyannamesi
Tartışma:Day After Day
Tartışma:Daşkesen
Tartışma:Taşkent (anlam ayrımı)
Tartışma:Damcılı
Tartışma:Dalga Arena
Tartışma:Dağ Üzü, Yardımlı
Tartışma:Brilliant Dadaşova
Tartışma:Cüve,Ağdaş
Tartışma:Azerbaycan kültürü
Tartışma:Çullu
Tartışma:Cücük, Ağdaş
Tartışma:Azerbaycan Cumhuriyeti Anayasası
Tartışma:Birinci Doğu Halkları Kurultayı
Tartışma:BDT Kupası
Tartışma:Çınarlı
Tartışma:Vatandaş Birliği Partisi
Tartışma:Cirimbel, Yardımlı
Tartışma:Çevgan
Tartışma:Çöğür
Tartışma:Çobanoğulları
Tartışma:Azerbaycan'da satranç
Tartışma:Mahmudali Çehregani
Tartışma:Yusuf Vezir Çemenzeminli
Tartışma:Çargah
Tartışma:Celilabad
Tartışma:Cebrayıl
Tartışma:Merkezi Hazar Diktatörlüğü
Tartışma:Azerbaycan Merkez Bankası
Tartışma:Çaylı
Tartışma:Çay Üzü, Yardımlı
Tartışma:Cavahirli
Tartışma:Kafkasya Üniversiteler Birliği
Tartışma:Kafkas Dağları
Tartışma:Kafkasya Almanları
Tartışma:Kafkasya
Tartışma:Jaycee Carroll
Tartışma:Cardam
Tartışma:Şuşa Muharebesi
Tartışma:Çanakbulak, Yardımlı
Tartışma:Azerbaycan Cumhuriyeti Bakanlar Kurulu
Tartışma:Buta Sarayı
Tartışma:Bürzünbül, Yardımlı
Tartışma:Polad Bülbüloğlu
Tartışma:Buduq, Kuba
Tartışma:Buduklular
Tartışma:Bozayran, Yardımlı
Tartışma:Bozavend
Tartışma:Nargin Adası
Tartışma:Böyük Oyun
Tartışma:Dede Korkut Kitabı
Tartışma:Siyah Şehir (Bakü)
Tartışma:Birinci Yüzbaşılı
Tartışma:Birinci Quzanlı
Tartışma:Birinci Dördyol
Tartışma:Birinci Baharlı
Tartışma:Binegedi
Tartışma:Bilne, Yardımlı
Tartışma:Bilesuvar
Tartışma:Bibiheybet Camii
Tartışma:Beydili
Tartışma:Bercan, Yardımlı
Tartışma:Beylegan
Tartışma:Nuri Berköz
Tartışma:Nergiz Birk-Petersen
Tartışma:Balaken Havalimanı
Tartışma:Ruşen Bayramov
Tartışma:Bakü Muharebesi (1918)
Tartışma:Başkent (anlam ayrımı)
Tartışma:Afak Seferova
Tartışma:Berhudarlı
Tartışma:Berde
Tartışma:Anatoliy Banişevskiy
Tartışma:Baltalı
Tartışma:Ballar
Tartışma:Balaken
Tartışma:Balaban (çalgı)
Tartışma:Bakü-Tiflis-Kars demiryolu hattı
Tartışma:Bakü-Tiflis-Ceyhan Petrol Boru Hattı
Tartışma:Bakü Televizyon Kulesi
Tartışma:Bakü Devlet Üniversitesi
Tartışma:Bakü Slavyan Üniversitesi
Tartışma:Azerbaycan Devlet Kukla Tiyatrosu
Tartışma:Bakü Olimpiyat Stadyumu
Tartışma:Bakü Modern Sanat Müzesi
Tartışma:Bakü metrosu
Tartışma:Bakü Hanlığı
Tartışma:Bakü Uluslararası Otobüs Terminali
Tartışma:Bakü Yüksek Petrol Okulu
Tartışma:Bakü Avrasya Üniversitesi
Tartışma:Kristal Salon (Bakü)
Tartışma:Bakü Şehir Pisti
Tartışma:Bakü 2020 Yaz Olimpiyatları adaylığı
Tartışma:Bakılı PFK
Tartışma:Bakcell Arena
Tartışma:Bakcell
Tartışma:Settar Behlulzade
Tartışma:Bahçelere Geldi Bahar
Tartışma:Baharlı, Ağdam
Tartışma:Babi Bedelov
Tartışma:Babı, Füzuli
Tartışma:Babek (şehir)
Tartışma:Refik Babayev
Tartışma:AzTV
Tartışma:Azıh Mağarası
Tartışma:Meşedi Azizbeyov
Tartışma:Azərpoçt
Tartışma:Azerbaycan Ulusal Marşı
Tartışma:Azerspace-1/Africasat-1a
Tartışma:Azeryol Bakü
Tartışma:Azer-Çırak-Güneşli Petrol Sahası
Tartışma:Azercell
Tartışma:Rusya Azerileri
Tartışma:Kırgızistan'daki Azeriler
Tartışma:Kazakistan'daki Azeriler
Tartışma:Almanya'daki Azeriler
Tartışma:Azerice Vikipedi
Tartışma:Azerbaycan Sovyet Ansiklopedisi
Tartışma:Azerbaycan halısı
Tartışma:2013 Azerbaycan cumhurbaşkanlığı seçimi
Tartışma:Azerbaycan Halk Cephesi Partisi
Tartışma:Azerbaycan pasaportu
Tartışma:Azerbaycan Deniz Kuvvetleri
Tartışma:Azerbaycan manatı
Tartışma:Azerice
Tartışma:Azerbaycan Kara Kuvvetleri
Tartışma:Azerbaycan'da Yılın Futbolcusu
Tartışma:Azeri Halk Oyunları
Tartışma:Azeri mutfağı
Tartışma:Azerbaycan Satranç Şampiyonası
Tartışma:Kanada'daki Azeriler
Tartışma:Azeri alfabesi
Tartışma:Azerbaycan-Türkiye ilişkileri
Tartışma:Azerbaycan–Gürcistan ilişkileri
Tartışma:Azerbaycan Kadınlar Voleybol Ligi
Tartışma:Azerbaycan Kadın Millî Futbol Takımı
Tartışma:Azerbaycan Diller Üniversitesi
Tartışma:Azerbaycan Mimarlık ve İnşaat Üniversitesi
Tartışma:Azerbaycan Superkuboku
Tartışma:Azerbaycan Devlet Genç Seyirciler Tiyatrosu
Tartışma:Azerbaycan Devlet Filarmonisi
Tartışma:Azerbaycan Devlet Petrol ve Sanayi Üniversitesi
Tartışma:Azerbaycan Devlet Denizcilik Akademisi
Tartışma:Azerbaycan Devlet Akademik Opera ve Bale Tiyatrosu
Tartışma:Azerbaycan Devlet Akademik Millî Dram Tiyatrosu
Tartışma:Azerbaycan 21 Yaş Altı Millî Futbol Takımı
Tartışma:Azerbaycan 19 Yaş Altı Millî Futbol Takımı
Tartışma:Azerbaycan Millî Ragbi Birliği Takımı
Tartışma:Azerbaycan Millî Futsal Takımı
Tartışma:Azerbaycan Millî Basketbol Takımı
Tartışma:Azerbaycan Milli Havacılık ve Uzay Ajansı
Tartışma:Azerbaycan Tıp Üniversitesi
Tartışma:Türkvizyon Şarkı Yarışması'nda Azerbaycan
Tartışma:Eurovision Çocuk Şarkı Yarışması'nda Azerbaycan
Tartışma:2017 Eurovision Şarkı Yarışması'nda Azerbaycan
Tartışma:2016 Eurovision Şarkı Yarışması'nda Azerbaycan
Tartışma:2015 Eurovision Şarkı Yarışması'nda Azerbaycan
Tartışma:2014 Eurovision Şarkı Yarışması'nda Azerbaycan
Tartışma:2013 Eurovision Şarkı Yarışması'nda Azerbaycan
Tartışma:2012 Eurovision Şarkı Yarışması'nda Azerbaycan
Tartışma:2011 Eurovision Şarkı Yarışması'nda Azerbaycan
Tartışma:2010 Eurovision Şarkı Yarışması'nda Azerbaycan
Tartışma:2009 Eurovision Şarkı Yarışması'nda Azerbaycan
Tartışma:2008 Eurovision Şarkı Yarışması'nda Azerbaycan
Tartışma:Eurovision Şarkı Yarışması'nda Azerbaycan
Tartışma:Bala Türkvizyon Şarkı Yarışması'nda Azerbaycan
Tartışma:Azerbaycan Futbol Akademisi
Tartışma:Azerbaycan Birinci Divizionu
Tartışma:Azerbaycan Kuboku
Tartışma:Azerbaycan Halı Müzesi
Tartışma:Olimpiyat Oyunları'nda Azerbaycan
Tartışma:2016 Yaz Olimpiyatları'nda Azerbaycan
Tartışma:2012 Yaz Olimpiyatları'nda Azerbaycan
Tartışma:2010 Kış Olimpiyatları'nda Azerbaycan
Tartışma:2010 Yaz Gençlik Olimpiyatları'nda Azerbaycan
Tartışma:2008 Yaz Olimpiyatları'nda Azerbaycan
Tartışma:2004 Yaz Olimpiyatları'nda Azerbaycan
Tartışma:1996 Yaz Olimpiyatları'nda Azerbaycan
Tartışma:Azerbaycan Hava Yolları
Tartışma:Azerbaycan (gazete)
Tartışma:Azerbaycan (İran)
Tartışma:AZAL PFK
Tartışma:AZAL Stadyumu
Tartışma:Azadlık (gazete)
Tartışma:Azadistan
Tartışma:Azad Azerbaycan TV
Tartışma:Eymür boyu
Tartışma:Ayrılık (şarkı)
Tartışma:Ayran
Tartışma:Avur, Yardımlı
Tartışma:Avun, Yardımlı
Tartışma:Avaş, Yardımlı
Tartışma:Atropatena
Tartışma:Ateşgah
Tartışma:Atabeg
Tartışma:Astara, Azerbaycan
Tartışma:Hezi Aslanov
Tartışma:Askeran
Tartışma:Askeran (kasaba)
Tartışma:İrade Aşumova
Tartışma:Âşık Garip
Tartışma:Aşık Garip (film)
Tartışma:Halk ozanı
Tartışma:Tuğrul Askerov
Tartışma:Azeri Lejyonu
Tartışma:Aşağıoba
Tartışma:Aşağı Yağlevend, Füzuli
Tartışma:Aybasanlı, Füzuli
Tartışma:Aşağı Astanlı, Yardımlı
Tartışma:Arvana, Yardımlı
Tartışma:Arış, Füzuli
Tartışma:Erdebil Hanlığı
Tartışma:Azerbaycan mimarisi
Tartışma:Region TV
Tartışma:Araz Naxçivan
Tartışma:Arayatlı, Füzuli
Tartışma:Aras Barajı ve Hidroelektrik Santrali
Tartışma:Hazar-Arap ilişkileri
Tartışma:Akkoyunlular
Tartışma:Anzov, Yardımlı
Tartışma:Azerbaycan Sovyet Sosyalist Cumhuriyeti ulusal marşı
Tartışma:ANS TV
Tartışma:ANS Şirketler Grubu
Tartışma:Ankara'dan Abim Geldi
Tartışma:Anbuba,Astara
Tartışma:Rahid Amirguliyev
Tartışma:Always (Aysel ve Arash şarkısı)
Tartışma:Allar, Yardımlı
Tartışma:Alıç
Tartışma:Alibeyli, Ağdam
Tartışma:Safura Alizade
Tartışma:Mihriban Aliyeva
Tartışma:Leyla Aliyeva (sunucu)
Tartışma:İlham Aliyev
Tartışma:Əlincə
Tartışma:Alibeyli
Tartışma:Aliağalı, Ağdam
Tartışma:Alçabulak, Yardımlı
Tartışma:Alazani
Tartışma:Vügar Alekberov
Tartışma:Şevket Alekberova
Tartışma:Ağstafa Havalimanı
Tartışma:Ekinci (gazete)
Tartışma:Mirza Fetali Ahundov
Tartışma:Ağsu
Tartışma:Ağstafa
Tartışma:Stratejik Ortaklık ve Karşılıklı Yardım Anlaşması
Tartışma:Ağulca
Tartışma:Ağstafaçay
Tartışma:Ahmed Ağdamski
Tartışma:Ağdaş
Tartışma:Ağdamkend, Ağdam
Tartışma:Ağçay, Kah
Tartışma:Ağçay (anlam ayrımı)
Tartışma:Ağcabedi
Tartışma:Emin Ağalarov
Tartışma:Afşar boyu
Tartışma:Afşarca
Tartışma:Afşar
Tartışma:Adıgüzelbeyli, Ağdam
Tartışma:ADA Üniversitesi
Tartışma:Ahameniş İmparatorluğu
Tartışma:Vusal Abdullazade
Tartışma:Rashad Abdullayev
Tartışma:Namık Abdullayev
Tartışma:Abdinli, Yardımlı
Tartışma:Abdal, Ağdam
Tartışma:Abbasabad, Yardımlı
Tartışma:Abayı
Tartışma:Abdulla Abatsiyev
Tartışma:Abalı
Tartışma:Patimat Abakarova
Tartışma:Abad,Ağdaş
Tartışma:2017 İslami Dayanışma Oyunları
Tartışma:2015 Avrupa Oyunları
Tartışma:2014-15 Azerbaycan Premyer Ligası
Tartışma:2013-14 Azerbaycan Premyer Ligası
Tartışma:2013-14 Azerbaycan Birinci Divizionu
Tartışma:2012-13 Azerbaycan Premyer Ligası
Tartışma:2012 Azerbaycan-Ermenistan sınır çatışmaları
Tartışma:2011-12 Azerbaycan Premyer Ligası
Tartışma:2011 Azerbaycan protestoları
Tartışma:2007 Dünya Güreş Şampiyonası
Tartışma:2006-07 Azerbaycan Yüksek Deste
Tartışma:1995 Bakü metro yangını
Tartışma:1995 Azerbaycan darbe girişimi
Tartışma:1994 Bakü Metrosu saldırıları
Tartışma:1992 Azerbaycan Yüksek Deste
Tartışma:26 Bakü Komiseri
Tartışma:3,14...
Tartışma:.az
Tartışma:Stratejik Ortaklık ve Karşılıklı Yardım Anlaşması
Tartışma:Ağulca
Tartışma:Ağstafaçay
Tartışma:Ahmed Ağdamski
Tartışma:Ağdaş
Tartışma:Ağdamkend, Ağdam
Tartışma:Ağçay, Kah
Tartışma:Ağçay (anlam ayrımı)
Tartışma:Ağcabedi
Tartışma:Emin Ağalarov
Tartışma:Afşar boyu
Tartışma:Afşarca
Tartışma:Afşar
Tartışma:Adıgüzelbeyli, Ağdam
Tartışma:ADA Üniversitesi
Tartışma:Ahameniş İmparatorluğu
Tartışma:Vusal Abdullazade
Tartışma:Rashad Abdullayev
Tartışma:Namık Abdullayev
Tartışma:Abdinli, Yardımlı
Tartışma:Abdal, Ağdam
Tartışma:Abbasabad, Yardımlı
Tartışma:Abayı
Tartışma:Abdulla Abatsiyev
Tartışma:Abalı
Tartışma:Patimat Abakarova
Tartışma:Abad,Ağdaş
Tartışma:2017 İslami Dayanışma Oyunları
Tartışma:2015 Avrupa Oyunları
Tartışma:2014-15 Azerbaycan Premyer Ligası
Tartışma:2013-14 Azerbaycan Premyer Ligası
Tartışma:2013-14 Azerbaycan Birinci Divizionu
Tartışma:2012-13 Azerbaycan Premyer Ligası
Tartışma:2012 Azerbaycan-Ermenistan sınır çatışmaları
Tartışma:2011-12 Azerbaycan Premyer Ligası
Tartışma:2011 Azerbaycan protestoları
Tartışma:2007 Dünya Güreş Şampiyonası
Tartışma:2006-07 Azerbaycan Yüksek Deste
Tartışma:1995 Bakü metro yangını
Tartışma:1995 Azerbaycan darbe girişimi
Tartışma:1994 Bakü Metrosu saldırıları
Tartışma:1992 Azerbaycan Yüksek Deste
Tartışma:26 Bakü Komiseri
Tartışma:3,14...
Tartışma:.az"""


for tr_talkpage in allpages.split('\n'):
    try:
        tr_page=tr_talkpage[11:]
        #print tr_page
        entity = mavri.wikibase_item('tr.wikipedia', tr_page)
        print entity
        en_page = mavri.wbgetlanglink(entity, 'enwiki')
        en_talkpage = 'Talk:'+en_page
        print en_talkpage
        content = requests.get('https://en.wikipedia.org/wiki/'+en_talkpage).text
        if "WikiProject Azerbaijan articles" not in content:
            print tr_talkpage
            text = '\n# [['+tr_talkpage+']]'
            mavri.appendtext_on_page('tr.wikipedia','Kullanıcı:Mavrikant/log', text, '', xx )
    except:
        print 'error'







