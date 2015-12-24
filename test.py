# -*- coding: utf-8 -*-

import json


with open('.pass') as data_file:
    data = json.load(data_file)

aaa= data['Mavrikant'].decode('base64').decode('base64').decode('base64').decode('UTF-8')
print aaa
print type(aaa)

