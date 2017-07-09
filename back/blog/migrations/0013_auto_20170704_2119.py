# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-04 18:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_image_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='body',
        ),
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(default='New post', max_length=40),
        ),
    ]
