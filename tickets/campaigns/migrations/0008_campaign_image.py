# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-20 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0007_liqpaydata_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='image',
            field=models.URLField(null=True),
        ),
    ]
