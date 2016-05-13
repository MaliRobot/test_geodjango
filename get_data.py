# -*- coding: utf-8 -*-
"""
Created on Wed May  4 19:39:03 2016

@author: Milosh
"""

import json
import urllib.request
import sys

def get_data(url, lst):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read().decode('utf-8'))
    
def main(mode):
    if mode == 'ug':
        out = open('user_geos.json', 'w', encoding='utf-8')
        url = 'https://represent.me/api/user_geos/'
    elif mode == 'rg':
        out = open('regions.json', 'w', encoding='utf-8')
        url = 'https://represent.me/api/geos/'
    else:
        return
        
    lst = []
    
    data = get_data(url, lst)
    for r in range(len(data['results'])):
        lst.append(data['results'][r]['url'])
    while data['next'] != None:
        url = data['next']
        data = get_data(url, lst)
        for r in range(len(data['results'])):
            lst.append(data['results'][r]['url'])
        print(url)
        print(len(lst))
    json.dump(lst, out)
    out.close()
    
if __name__ == '__main__':
    main(sys.argv[1:])