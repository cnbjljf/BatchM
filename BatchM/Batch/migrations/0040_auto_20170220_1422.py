# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-20 06:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Batch', '0039_auto_20170217_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approvehosts',
            name='asset_id',
            field=models.CharField(max_length=4096),
        ),
        migrations.AlterField(
            model_name='approvehosts',
            name='minion_name',
            field=models.CharField(max_length=4096),
        ),
        migrations.AlterField(
            model_name='workorderofupdate',
            name='OrderId',
            field=models.CharField(default='20170220142214', max_length=128, primary_key=True, serialize=False, verbose_name='工单ID'),
        ),
    ]
