# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-11-03 11:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spidey', '0004_safescanresult'),
    ]

    operations = [
        migrations.AddField(
            model_name='safescanresult',
            name='lastscantime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]