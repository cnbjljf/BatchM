# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-20 07:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Batch', '0043_auto_20170220_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='newassetapprovalzone',
            name='salt_minion_id',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='saltstack_minion_id'),
        ),
        migrations.AlterField(
            model_name='workorderofupdate',
            name='OrderId',
            field=models.CharField(default='20170220150414', max_length=128, primary_key=True, serialize=False, verbose_name='工单ID'),
        ),
    ]
