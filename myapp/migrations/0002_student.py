# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-23 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollNumber', models.CharField(max_length=30)),
                ('meritStatus', models.IntegerField()),
            ],
        ),
    ]