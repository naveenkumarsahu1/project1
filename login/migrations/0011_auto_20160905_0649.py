# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-05 06:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_auto_20160905_0626'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=10)),
                ('contactname', models.CharField(max_length=15)),
                ('mobilenumber', models.CharField(max_length=12)),
            ],
        ),
        migrations.AlterField(
            model_name='usergroup',
            name='groupid',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='usergroup',
            name='userid',
            field=models.CharField(max_length=10),
        ),
    ]