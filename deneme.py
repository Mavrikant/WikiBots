# -*- coding: utf-8 -*-
# !/usr/bin/python

import mavri

xx = mavri.login('tr.wikipedia', 'Mavrikant Bot')

print xx.text
print mavri.appendtext_on_page('tr.wikipedia', 'Vikipedi:Deneme tahtası', 'test', 'test', xx).text
exit(0)
