# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-20 06:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Batch', '0040_auto_20170220_1422'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='approvehosts',
            options={'verbose_name': '批准主机的数量', 'verbose_name_plural': '批准主机的数量'},
        ),
        migrations.AlterField(
            model_name='approvehosts',
            name='asset_id',
            field=models.CharField(max_length=4096, verbose_name='资产ID'),
        ),
        migrations.AlterField(
            model_name='approvehosts',
            name='minion_name',
            field=models.CharField(max_length=4096, verbose_name='saltstack_minion_name'),
        ),
        migrations.AlterField(
            model_name='workorderofupdate',
            name='OrderId',
            field=models.CharField(default='20170220142906', max_length=128, primary_key=True, serialize=False, verbose_name='工单ID'),
        ),
    ]
