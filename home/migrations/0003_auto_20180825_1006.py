# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-08-25 04:36
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20180825_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='club_image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
