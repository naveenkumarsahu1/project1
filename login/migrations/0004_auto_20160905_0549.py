# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-05 05:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20160905_0539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupid1',
            name='MobileNo',
            field=models.BigIntegerField(max_length=10),
        ),
    ]