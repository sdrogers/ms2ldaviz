# Generated by Django 3.0.6 on 2021-01-09 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ms1analysis', '0008_auto_20170509_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysis',
            name='status',
            field=models.CharField(choices=[('0', 'Pending'), ('1', 'Ready')], default='1', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='decompositionanalysis',
            name='status',
            field=models.CharField(choices=[('0', 'Pending'), ('1', 'Ready')], default='1', max_length=128, null=True),
        ),
    ]