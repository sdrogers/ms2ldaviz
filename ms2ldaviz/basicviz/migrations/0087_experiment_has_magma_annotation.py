# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-10-17 16:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicviz', '0086_auto_20181016_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='has_magma_annotation',
            field=models.BooleanField(default=False),
        ),
    ]
