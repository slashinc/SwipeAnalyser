# Generated by Django 2.0.1 on 2018-02-12 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_employee_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='document',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.Document'),
        ),
        migrations.AddField(
            model_name='employeecomplete',
            name='document',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.Document'),
        ),
    ]
