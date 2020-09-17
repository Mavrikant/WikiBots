# -*- coding: utf-8 -*-
# !/usr/bin/python

import re
import requests
import mavri
import pandas as pd
import ray
import time

ray.init()
wiki = 'tr.wikipedia'
xx = mavri.login(wiki, 'Mavrikant Bot')
months = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık']

@ray.remote
def  process(title,text):
    if(mavri.content_of_page(wiki,title)==""):
        mavri.appendtext_on_page(wiki,title,text,"Yeni kategori",xx)
        return title+":"+"empty"
    else:
        return  "****"+title+":"+mavri.content_of_page(wiki,title)

      


output_ids = []
if __name__ == '__main__':
    for year in range(2024,2026):
        for iteration, month in enumerate(months):
            title="Kategori:Kaynakları olmayan maddeler {} {}".format(month, year)
            text="__HIDDENCAT__\n[[Kategori:Kaynakları olmayan maddeler |{}{:02d}]]".format(year,iteration+1)
            output_ids.append(process.remote(title,text))
    
    output_list = ray.get(output_ids)
    for lista in output_list:
        print lista