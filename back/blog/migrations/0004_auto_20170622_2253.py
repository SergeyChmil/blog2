# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 19:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170622_2249'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='icon',
            new_name='city',
        ),
    ]