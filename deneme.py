# -*- coding: utf-8 -*-
# !/usr/bin/python

import mavri

xx = mavri.login(u'tr.wikipedia', u'Mavrikant Bot')

print xx.text
print mavri.appendtext_on_page(u'tr.wikipedia', u'Vikipedi:Deneme tahtası', u'test', u'test', xx).text
