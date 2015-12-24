# -*- coding: utf-8 -*-
import json

with open(".pass") as json_file:
    json_data = json.load(json_file)

passw = json_data['Mavrikant'].decode('base64').decode('base64').decode('base64').decode('UTF-8')
print passw
print type(passw)
