# Generated by Django 2.1.5 on 2019-02-06 22:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dating_forms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datingform',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 2, 7, 1, 16, 29, 832445)),
        ),
    ]