# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-23 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0012_auto_20160520_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='something',
            field=models.CharField(default='<no text>', max_length=200),
        ),
    ]