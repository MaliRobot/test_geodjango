# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-10 21:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_rest', '0008_auto_20160510_1920'),
    ]

    operations = [
        migrations.RenameField(
            model_name='geom',
            old_name='json_data',
            new_name='geom',
        ),
    ]
