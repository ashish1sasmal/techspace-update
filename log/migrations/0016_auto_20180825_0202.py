# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-24 20:32
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0015_auto_20180825_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name=b'image'),
        ),
    ]
