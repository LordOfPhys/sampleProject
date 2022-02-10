# Generated by Django 4.0.2 on 2022-02-10 06:10

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outlet',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outlets_employee', to='app.employee'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='date',
            field=models.DateField(default=datetime.date(2022, 2, 10)),
        ),
    ]