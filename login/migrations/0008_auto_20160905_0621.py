# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-05 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20160905_0619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergroup',
            name='userid',
            field=models.BigIntegerField(),
        ),
    ]
