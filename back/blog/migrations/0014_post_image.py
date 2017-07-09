# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-04 18:29
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20170704_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=blog.models.scramble_uploaded_image_name, verbose_name='Uploaded Image'),
        ),
    ]
