# Generated by Django 4.0.2 on 2022-02-10 06:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_visit_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outlet',
            name='label',
        ),
        migrations.AddField(
            model_name='outlet',
            name='name',
            field=models.CharField(default='name', max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(default='name', max_length=100),
        ),
        migrations.AlterField(
            model_name='visit',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 2, 10, 6, 39, 19, 166873, tzinfo=utc)),
        ),
    ]
