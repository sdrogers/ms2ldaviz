# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-10-16 11:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicviz', '0084_auto_20181015_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featureinstance2sub',
            name='fragatoms',
            field=models.CharField(max_length=1024),
        ),
    ]