# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-27 23:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app03', '0009_auto_20171227_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='consultant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app03.UserInfo', verbose_name='课程顾问'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_consult_date',
            field=models.DateField(blank=True, null=True, verbose_name='最后跟进日期'),
        ),
    ]
