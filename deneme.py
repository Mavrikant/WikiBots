# -*- coding: utf-8 -*-

import mavri

xx = mavri.login('tr.wikipedia', 'Mavrikant Bot')

print mavri.appendtext_on_page('tr.wikipedia', 'Vikipedi:Deneme tahtası', 'test', 'test', xx).text
