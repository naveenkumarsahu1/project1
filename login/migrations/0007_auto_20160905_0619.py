# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-05 06:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_groupid2_groupid3'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupid', models.BigIntegerField()),
                ('userid', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Groupid1',
        ),
        migrations.DeleteModel(
            name='Groupid2',
        ),
        migrations.DeleteModel(
            name='Groupid3',
        ),
    ]