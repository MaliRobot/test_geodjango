# -*- coding: utf-8 -*-
"""
Created on Wed May  4 19:39:03 2016

@author: Milosh
"""

import json
import urllib.request

def get_data(url, lst):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read().decode('utf-8'))
    
def main():
    out = open('regions_geom.json', 'w', encoding='utf-8')
    url = 'https://represent.me/api/geos/'
        
    lst = []
    
    data = get_data(url, lst)
    for r in range(len(data['results'])):
        lst.append([data['results'][r]['id'], data['results'][r]['geom']])
    while data['next'] != None:
        url = data['next']
        data = get_data(url, lst)
        for r in range(len(data['results'])):
            lst.append([data['results'][r]['id'], data['results'][r]['geom']])
        print(url)
        print(len(lst))
    json.dump(lst, out)
    out.close()
    
if __name__ == '__main__':
    main()