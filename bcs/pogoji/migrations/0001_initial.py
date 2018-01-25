# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-25 20:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dolocilo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stevilka', models.IntegerField(null=True)),
                ('koda', models.CharField(max_length=100, null=True)),
                ('opis', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pogoj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stevilka', models.IntegerField(null=True)),
                ('koda', models.CharField(max_length=100, null=True)),
                ('opis', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SkupinaDolocila',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stevilka', models.IntegerField(null=True)),
                ('koda', models.CharField(max_length=100, null=True)),
                ('opis', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SkupinaPogoja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stevilka', models.IntegerField(null=True)),
                ('koda', models.CharField(max_length=100, null=True)),
                ('opis', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='pogoj',
            name='skupinapogoja',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pogoji.SkupinaPogoja'),
        ),
        migrations.AddField(
            model_name='dolocilo',
            name='skupinadolocila',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pogoji.SkupinaDolocila'),
        ),
    ]
