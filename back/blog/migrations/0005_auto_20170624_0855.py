# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-24 05:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170622_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='region',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.Region'),
        ),
    ]
