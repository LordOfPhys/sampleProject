# Generated by Django 4.0.2 on 2022-02-10 06:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_employee_outlet_e_alter_visit_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outlet',
            name='label',
            field=models.CharField(default='label', max_length=100),
        ),
        migrations.AlterField(
            model_name='visit',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 2, 10, 6, 24, 56, 314967, tzinfo=utc)),
        ),
    ]
