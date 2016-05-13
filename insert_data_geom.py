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

from test_rest.models import Geom
from django.contrib.gis.geos import Polygon, MultiPolygon

def main():
    geos_file = open('regions_geom.json', 'r', encoding='utf-8')
    
    geos_data = json.load(geos_file)
    i = 0
    for url in geos_data:
        print(i)
        geom = Geom()
        geom.id = url[0]
        geom.geom = url[1]
        i += 1
        geom.save()

if __name__ == '__main__':
    main()