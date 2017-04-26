# -*- coding: utf-8 -*-
# !/usr/bin/python

import json
import os
import re
import sys

import requests

reload(sys)
sys.setdefaultencoding('UTF8')


def login(wiki, username):
    full_path = os.path.realpath(__file__)
    with open(os.path.dirname(full_path) + '/.pass') as data_file:
        data = json.load(data_file)
    passw = data[username].decode('base64').decode('base64').decode('base64').decode('UTF-8')

    payload = {'action': 'query', 'format': 'json', 'utf8': '', 'meta': 'tokens', 'type': 'login'}
    r1 = requests.post('https://' + wiki + '.org/w/api.php', data=payload)

    login_token = r1.json()['query']['tokens']['logintoken']
    payload = {'action': 'login', 'format': 'json', 'utf8': '', 'lgname': username, 'lgpassword': passw,
               'lgtoken': login_token}
    return requests.post('https://' + wiki + '.org/w/api.php', data=payload, cookies=r1.cookies)


def appendtext_on_page(wiki, title, appendtext, summary, xx):
    params3 = '?format=json&action=tokens'
    r3 = requests.get('https://' + wiki + '.org/w/api.php' + params3, cookies=xx.cookies)
    edit_token = r3.json()['tokens']['edittoken']
    edit_cookie = xx.cookies.copy()
    edit_cookie.update(r3.cookies)

    payload = {'action': 'edit', 'assert': 'user', 'format': 'json', 'utf8': '', 'appendtext': appendtext,
               'summary': summary,
               'title': title, 'token': edit_token, 'bot': ''}
    return requests.post('https://' + wiki + '.org/w/api.php', data=payload, cookies=edit_cookie)


def wikibase_item(wiki, title):
    try:
        return requests.get(
            'https://' + wiki + '.org/w/api.php?action=query&utf8&format=json&prop=pageprops&titles=' + title).json()[
            'query']['pages'].itervalues().next()['pageprops']['wikibase_item']
    except:
        return ''


def sent_message(wiki, title, appendtext, summary, xx):
    return appendtext_on_page(wiki, title, appendtext, summary, xx)


def change_page(wiki, title, text, summary, xx):
    params3 = '?format=json&action=tokens'
    r3 = requests.get('https://' + wiki + '.org/w/api.php' + params3, cookies=xx.cookies)
    edit_token = r3.json()['tokens']['edittoken']
    edit_cookie = xx.cookies.copy()
    edit_cookie.update(r3.cookies)

    payload = {'action': 'edit', 'assert': 'user', 'format': 'json', 'utf8': '', 'text': text,
               'summary': summary,
               'title': title, 'token': edit_token, 'bot': ''}
    return requests.post('https://' + wiki + '.org/w/api.php', data=payload, cookies=edit_cookie)


def page_clear(wiki, title, summary, xx):
    return change_page(wiki, title, '', summary, xx)


def change_section(wiki, title, section, content, summary, xx):
    params3 = '?format=json&action=tokens'
    r3 = requests.get('https://' + wiki + '.org/w/api.php' + params3, cookies=xx.cookies)
    edit_token = r3.json()['tokens']['edittoken']
    edit_cookie = xx.cookies.copy()
    edit_cookie.update(r3.cookies)

    payload = {'action': 'edit', 'assert': 'user', 'format': 'json', 'utf8': '', 'section': str(section),
               'text': content,
               'summary': summary, 'title': title, 'token': edit_token, 'bot': ''}
    return requests.post('https://' + wiki + '.org/w/api.php', data=payload, cookies=edit_cookie)


def section_clear(wiki, title, section, summary, xx):
    change_section(wiki, title, section, '', summary, xx)


def blocked(wiki, vandal):
    params4 = '?format=json&utf8=&action=query&list=blocks&bkprop=id%7Cuser%7Cby%7Ctimestamp%7Cexpiry%7Creason%7Crange%7Cflags&bkusers='
    return requests.get('https://' + wiki + '.org/w/api.php' + params4 + vandal)


def random_page(wiki):
    return \
        requests.get(
            'https://' + wiki + '.org/w/api.php?format=json&utf8=&action=query&list=random&rnnamespace=0').json()[
            'query']['random'][0]['title']


def categories_on_page(wiki, title):
    catNS = requests.get(
        'https://' + wiki + '.org/w/api.php?format=json&utf8=&action=query&meta=siteinfo&siprop=namespaces').json()[
        'query']['namespaces']['14']['*']
    content = content_of_page(wiki, title)
    return re.findall(r'\[\[\s?' + catNS + '\s?:\s?([^\[\|\]]*)\s?', content)


def content_of_page(wiki, title):
    return requests.get('https://' + wiki + '.org/w/index.php?title=' + title + '&action=raw').text


def content_of_section(wiki, title, section, xx):
    try:
        return requests.get(
            'https://' + wiki + '.org/w/api.php?format=json&utf8=&action=query&prop=revisions&rvprop=content&rvsection=' + str(
                section) + '&titles=' + title).json()['query']['pages'].itervalues().next()['revisions'][0]['*']
    except:
        return ''


def review_diff(wiki, diff, xx):
    params3 = '?format=json&action=query&meta=tokens'
    r3 = requests.get('https://' + wiki + '.org/w/api.php' + params3, cookies=xx.cookies)
    token = r3.json()['query']['tokens']['csrftoken']

    review_cookies = xx.cookies.copy()
    review_cookies.update(r3.cookies)
    payload = {'action': 'review', 'format': 'json', 'revid': int(diff), 'token': token}
    return requests.post('https://' + wiki + '.org/w/api.php', data=payload, cookies=review_cookies)


def wbcreateclaim(entity, property, snaktype, value, xx):
    wiki = 'www.wikidata'
    params3 = '?format=json&action=query&meta=tokens'
    r3 = requests.get('https://' + wiki + '.org/w/api.php' + params3, cookies=xx.cookies)
    token = r3.json()['query']['tokens']['csrftoken']
    edit_cookie = xx.cookies.copy()
    edit_cookie.update(r3.cookies)

    payload = {'action': 'wbcreateclaim', 'format': 'json', 'utf8': '', 'entity': entity, 'property': property,
               'snaktype': snaktype, 'value': '"' + value + '"', 'token': token, 'bot': ''}
    return requests.post('https://' + wiki + '.org/w/api.php', data=payload, cookies=edit_cookie)


def wbgetclaims(entity, property):
    wiki = 'www.wikidata'

    payload = {'action': 'wbgetclaims', 'format': 'json', 'utf8': '', 'entity': entity, 'property': property}
    return requests.post('https://' + wiki + '.org/w/api.php', data=payload)


def wbsetsitelink(entity, linksite, linktitle, xx):
    wiki = 'www.wikidata'
    params3 = '?format=json&action=query&meta=tokens'
    r3 = requests.get('https://' + wiki + '.org/w/api.php' + params3, cookies=xx.cookies)
    token = r3.json()['query']['tokens']['csrftoken']
    edit_cookie = xx.cookies.copy()
    edit_cookie.update(r3.cookies)

    payload = {'action': 'wbsetsitelink', 'format': 'json', 'utf8': '', 'id': entity, 'linksite': linksite,
               'linktitle': linktitle, 'token': token, 'bot': ''}
    return requests.post('https://' + wiki + '.org/w/api.php', data=payload, cookies=edit_cookie)


def wbmergeitems(fromid, toid, xx):
    wiki = 'www.wikidata'
    params3 = '?format=json&action=query&meta=tokens'
    r3 = requests.get('https://' + wiki + '.org/w/api.php' + params3, cookies=xx.cookies)
    token = r3.json()['query']['tokens']['csrftoken']
    edit_cookie = xx.cookies.copy()
    edit_cookie.update(r3.cookies)

    payload = {'action': 'wbmergeitems', 'format': 'json', 'utf8': '', 'fromid': fromid, 'toid': toid, 'token': token,
               'bot': ''}
    return requests.post('https://' + wiki + '.org/w/api.php', data=payload, cookies=edit_cookie)


def wbgetlanglink(entity, lang):
    wiki = 'www.wikidata'

    payload = {'action': 'wbgetentities', 'format': 'json', 'utf8': '', 'ids': entity, 'props': 'sitelinks'}
    try:
        return \
            requests.post('https://' + wiki + '.org/w/api.php', data=payload).json()['entities'][
                entity][
                'sitelinks'][lang]['title']
    except KeyError:
        return ''


def wbgetlangsofentity(entity):
    wiki = 'www.wikidata'

    payload = {'action': 'wbgetentities', 'format': 'json', 'utf8': '', 'ids': entity, 'props': 'sitelinks'}
    try:
        content = requests.post('https://' + wiki + '.org/w/api.php', data=payload).text
        return re.findall('\"site\":\"([^\"]*)\"', content)
    except KeyError:
        return ''


def wbremoveclaims(claim, xx):
    wiki = 'www.wikidata'
    params3 = '?format=json&action=query&meta=tokens'
    r3 = requests.get('https://' + wiki + '.org/w/api.php' + params3, cookies=xx.cookies)
    token = r3.json()['query']['tokens']['csrftoken']
    edit_cookie = xx.cookies.copy()
    edit_cookie.update(r3.cookies)

    payload = {'action': 'wbremoveclaims', 'format': 'json', 'utf8': '', 'claim': claim, 'token': token, 'bot': ''}
    return requests.post('https://' + wiki + '.org/w/api.php', data=payload, cookies=edit_cookie)


def wbsetclaimvalue(claim, snaktype, value, xx):
    wiki = 'www.wikidata'
    params3 = '?format=json&action=query&meta=tokens'
    r3 = requests.get('https://' + wiki + '.org/w/api.php' + params3, cookies=xx.cookies)
    token = r3.json()['query']['tokens']['csrftoken']
    edit_cookie = xx.cookies.copy()
    edit_cookie.update(r3.cookies)

    payload = {'action': 'wbsetclaimvalue', 'format': 'json', 'utf8': '', 'claim': claim, 'snaktype': snaktype,
               'value': '"' + value + '"', 'token': token, 'bot': ''}
    return requests.post('https://' + wiki + '.org/w/api.php', data=payload, cookies=edit_cookie)


def pages_on_category(wiki, category):
    params = '?format=json&utf8=&action=query&list=categorymembers&cmtitle=' + category + '&cmlimit=5000'
    return requests.get('https://' + wiki + '.org/w/api.php' + params).json()['query']['categorymembers']


def embeddedin(wiki, page):
    params = '?format=json&utf8=&action=query&list=embeddedin&eititle=' + page + '&eilimit=5000'
    return requests.get('https://' + wiki + '.org/w/api.php' + params).json()['query']['embeddedin']
