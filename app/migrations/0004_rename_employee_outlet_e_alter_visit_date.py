# Generated by Django 4.0.2 on 2022-02-10 06:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_visit_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='outlet',
            old_name='employee',
            new_name='e',
        ),
        migrations.AlterField(
            model_name='visit',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 2, 10, 6, 16, 27, 977198, tzinfo=utc)),
        ),
    ]