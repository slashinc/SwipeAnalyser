# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-03 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20171004_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='processed',
            field=models.BooleanField(default=False),
        ),
    ]
