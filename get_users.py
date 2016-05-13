# -*- coding: utf-8 -*-
"""
Created on Wed May  4 19:39:03 2016

@author: Milosh
"""

import json
import urllib.request

def get_data(url):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read().decode('utf-8'))
    
def main():
    out = open('users.json', 'w', encoding='utf-8')
    url = 'https://represent.me/api/users/'
        
    lst = []
    
    data = get_data(url)
    for r in range(len(data['results'])):
        lst.append([data['results'][r]['dob'], data['results'][r]['gender'], data['results'][r]['url']])
    while data['next'] != None:
        url = data['next']
        data = get_data(url)
        for r in range(len(data['results'])):
            lst.append([data['results'][r]['dob'], data['results'][r]['gender'], data['results'][r]['url']])
        print(url)
        print(len(lst))
    json.dump(lst, out)
    out.close()
    
if __name__ == '__main__':
    main()