# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-21 10:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('specifikacije', '0002_auto_20171221_1014'),
    ]

    operations = [
        migrations.RenameField(
            model_name='specifikacija',
            old_name='predmet_specifikacije',
            new_name='predmet',
        ),
    ]