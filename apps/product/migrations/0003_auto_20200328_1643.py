# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-03-28 08:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_prodpartner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prodpartner',
            old_name='user',
            new_name='pro_user',
        ),
    ]