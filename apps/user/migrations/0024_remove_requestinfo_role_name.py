# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-03-28 06:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0023_auto_20200328_1224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestinfo',
            name='role_name',
        ),
    ]