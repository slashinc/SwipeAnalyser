# Generated by Django 2.0.1 on 2018-01-30 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_create-superuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='code',
            field=models.CharField(blank=True, max_length=1),
        ),
    ]
