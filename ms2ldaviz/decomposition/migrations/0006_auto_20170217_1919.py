# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-17 19:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicviz', '0049_auto_20170216_2228'),
        ('decomposition', '0005_beta_alpha_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentGlobalMass2Motif',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('probability', models.FloatField()),
                ('overlap_score', models.FloatField()),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basicviz.Document')),
                ('mass2motif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decomposition.GlobalMotif')),
            ],
        ),
        migrations.RemoveField(
            model_name='globalmotifglobalfeature',
            name='feature',
        ),
        migrations.RemoveField(
            model_name='globalmotifglobalfeature',
            name='motif',
        ),
        migrations.DeleteModel(
            name='GlobalMotifGlobalFeature',
        ),
    ]