# -*- coding: utf-8 -*-
"""
Created on Fri May  6 01:16:44 2016

@author: Milosh
"""

import json, os, sys
import django
import urllib.request
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SYS_PATH = os.path.dirname(BASE_DIR)
if SYS_PATH not in sys.path:
    sys.path.append(SYS_PATH)
os.environ['DJANGO_SETTINGS_MODULE'] = 'test_project.settings'
django.setup()

from test_rest.models import User

def calculate_age(born):
    print(born)
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def main():
    users_file = open('users.json', 'r', encoding='utf-8')
    
    users_data = json.load(users_file)
    i = 0
    for user in users_data:
        # print(i)
        usr = User()
        id = user[2].split('/')[-2]
        print(id)
        usr.id = int(id)
        usr.gender = user[1]
        birth = user[0]
        if birth != None:
            birth = datetime.datetime.strptime(birth.replace('-',''), '%Y%m%d').date()
            usr.age = calculate_age(birth)
        else:
            usr.age = -1
        # i += 1
        usr.save()

if __name__ == '__main__':
    main()