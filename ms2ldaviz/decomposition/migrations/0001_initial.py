# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-17 10:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('basicviz', '0049_auto_20170216_2228'),
    ]

    operations = [
        migrations.CreateModel(
            name='Decomposition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('experiment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basicviz.Experiment')),
            ],
        ),
        migrations.CreateModel(
            name='DecompositionFeatureInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intensity', models.FloatField()),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basicviz.Document')),
            ],
        ),
        migrations.CreateModel(
            name='DocumentGlobalFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intensity', models.FloatField()),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basicviz.Document')),
            ],
        ),
        migrations.CreateModel(
            name='FeatureMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='FeatureSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=1024, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GlobalFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('min_mz', models.FloatField()),
                ('max_mz', models.FloatField()),
                ('featureset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decomposition.FeatureSet')),
            ],
        ),
        migrations.CreateModel(
            name='GlobalMotif',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('originalmotif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basicviz.Mass2Motif')),
            ],
        ),
        migrations.CreateModel(
            name='GlobalMotifGlobalFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('probability', models.FloatField()),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decomposition.GlobalFeature')),
                ('motif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decomposition.GlobalMotif')),
            ],
        ),
        migrations.AddField(
            model_name='featuremap',
            name='globalfeature',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decomposition.GlobalFeature'),
        ),
        migrations.AddField(
            model_name='featuremap',
            name='localfeature',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basicviz.Feature'),
        ),
        migrations.AddField(
            model_name='documentglobalfeature',
            name='feature',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decomposition.GlobalFeature'),
        ),
        migrations.AddField(
            model_name='decompositionfeatureinstance',
            name='feature',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decomposition.GlobalFeature'),
        ),
    ]
