# Generated by Django 4.0.2 on 2022-02-10 06:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_outlet_label_alter_visit_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 2, 10, 6, 36, 50, 569455, tzinfo=utc)),
        ),
    ]