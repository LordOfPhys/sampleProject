# Generated by Django 4.0.2 on 2022-02-10 07:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_visit_date_alter_visit_visit_outlet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 2, 10, 7, 21, 13, 870219, tzinfo=utc)),
        ),
    ]
