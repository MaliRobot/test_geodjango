# -*- coding: utf-8 -*-
"""
Created on Fri May  6 01:16:44 2016

@author: Milosh
"""

import json, os, sys
import django
import urllib.request


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SYS_PATH = os.path.dirname(BASE_DIR)
if SYS_PATH not in sys.path:
    sys.path.append(SYS_PATH)
os.environ['DJANGO_SETTINGS_MODULE'] = 'test_project.settings'
django.setup()

from test_rest.models import User_geos, Geos, Geos_Multi
from django.contrib.gis.geos import Polygon, MultiPolygon

def main():
    geos_file = open('regions.json', 'r', encoding='utf-8')
    users_file = open('user_geos.json', 'r', encoding='utf-8')
    
    geos_data = json.load(geos_file)
    users_data = json.load(users_file)
    i = 0
    for url in geos_data:
        req = urllib.request.Request(url)
        geos = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
#        print(geos)
        print(i)
        i += 1
        if geos['geom']['type'] == 'Polygon':
            geos_inst = Geos()
            geos_inst.id = geos['id']
            geos_inst.url = geos['url']
            geos_inst.ID = geos['ID']
            geos_inst.name = geos['name']
            geos_inst.m_type = geos['m_type']
            geos_inst.coordinates = Polygon(tuple(tuple(x) for x in geos['geom']['coordinates'][0]))
            geos_inst.created_at = geos['created_at']
            geos_inst.modified_at = geos['modified_at']
            geos_inst.save()
        else:
            geos_inst = Geos_Multi()
            geos_inst.id = geos['id']
            geos_inst.url = geos['url']
            geos_inst.ID = geos['ID']
            geos_inst.name = geos['name']
            geos_inst.m_type = geos['m_type']
            # multi = []
            # for poly in geos['geom']['coordinates']:
            #     for p in poly:
            #         multi.append(tuple(tuple(x) for x in p))
            # print(len(multi))
            # geos_inst.coordinates = MultiPolygon(tuple(tuple(multi)))
            geos_inst.created_at = geos['created_at']
            geos_inst.modified_at = geos['modified_at']
            geos_inst.save()
        
    # i = 0
#     for url in users_data:
#         req = urllib.request.Request(url)
#         geos = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
# #        print(geos)
#         print(i)
#         i += 1
#         user_geos_inst = User_geos()
#         user_geos_inst.id = geos['id']
#         user_geos_inst.url = geos['url']
#         user_geos_inst.geo = geos['geo']
#         user_geos_inst.user = geos['user']
#         user_geos_inst.user_url = geos['user_url']
#         user_geos_inst.created_at = geos['created_at']
#         user_geos_inst.modified_at = geos['modified_at']
#         user_geos_inst.save()

if __name__ == '__main__':
    main()