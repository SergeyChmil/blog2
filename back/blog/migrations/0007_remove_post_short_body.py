# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-24 09:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20170624_0858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='short_body',
        ),
    ]