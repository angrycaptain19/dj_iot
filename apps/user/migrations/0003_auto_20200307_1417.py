# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-03-07 06:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200307_1206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='name',
            new_name='department_name',
        ),
    ]
