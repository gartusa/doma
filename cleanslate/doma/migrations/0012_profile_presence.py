# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-28 05:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doma', '0011_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='presence',
            field=models.BooleanField(default=False, help_text='Do you smoke cigarettes?'),
        ),
    ]
