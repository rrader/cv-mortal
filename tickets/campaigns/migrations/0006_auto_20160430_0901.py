# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-30 09:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0005_auto_20160430_0749'),
    ]

    operations = [
        migrations.CreateModel(
            name='LiqPayData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lp_action', models.CharField(max_length=50, null=True)),
                ('lp_amount', models.DecimalField(decimal_places=2, max_digits=8, null=True)),
                ('lp_code', models.CharField(max_length=50, null=True)),
                ('lp_currency', models.CharField(max_length=50, null=True)),
                ('lp_err_code', models.CharField(max_length=50, null=True)),
                ('lp_err_description', models.CharField(max_length=255, null=True)),
                ('lp_ip', models.CharField(max_length=50, null=True)),
                ('lp_liqpay_order_id', models.CharField(max_length=50, null=True)),
                ('lp_payment_id', models.IntegerField(null=True)),
                ('lp_paytype', models.CharField(max_length=50, null=True)),
                ('lp_public_key', models.CharField(max_length=50, null=True)),
                ('lp_sender_card_mask2', models.CharField(max_length=50, null=True)),
                ('lp_status', models.CharField(max_length=50, null=True)),
                ('lp_transaction_id', models.CharField(max_length=50, null=True)),
                ('lp_type', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='cart',
            name='lp_action',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='lp_amount',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='lp_code',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='lp_currency',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='lp_err_code',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='lp_err_description',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='lp_ip',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='lp_liqpay_order_id',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='lp_payment_id',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='lp_paytype',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='lp_public_key',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='lp_sender_card_mask2',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='lp_status',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='lp_transaction_id',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='lp_type',
        ),
        migrations.AddField(
            model_name='liqpaydata',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaigns.Cart'),
        ),
    ]