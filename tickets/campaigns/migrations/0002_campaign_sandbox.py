# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='sandbox',
            field=models.BooleanField(default=True),
        ),
    ]