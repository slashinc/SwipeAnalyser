# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-08 10:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='employee_name',
        ),
    ]
