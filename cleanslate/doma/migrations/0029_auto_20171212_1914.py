# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-13 00:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doma', '0028_auto_20171212_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='/media/avatars/default.jpg', upload_to='avatars/upload/'),
        ),
    ]
