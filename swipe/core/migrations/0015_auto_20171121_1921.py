# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-21 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20171121_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeecomplete',
            name='empid',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]