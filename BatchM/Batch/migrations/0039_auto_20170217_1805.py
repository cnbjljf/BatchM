# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-17 10:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Batch', '0038_auto_20170217_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApproveHosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('how_many', models.IntegerField()),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='批准时间')),
                ('asset_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Batch.Asset', verbose_name='资产编号')),
                ('minion_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Batch.SaltstackMinions', verbose_name='Minion的主机名')),
            ],
        ),
        migrations.AlterField(
            model_name='workorderofupdate',
            name='OrderId',
            field=models.CharField(default='20170217180502', max_length=128, primary_key=True, serialize=False, verbose_name='工单ID'),
        ),
    ]
