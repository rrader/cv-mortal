# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-20 14:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0009_campaign_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='goal',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
