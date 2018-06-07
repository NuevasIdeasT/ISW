# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-07 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Activities', '0005_auto_20180507_1221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='Instructor',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='Type',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='Ubicacion',
        ),
        migrations.RemoveField(
            model_name='empleados',
            name='ID',
        ),
        migrations.RemoveField(
            model_name='tiposact',
            name='ID',
        ),
        migrations.RemoveField(
            model_name='ubicacion',
            name='ID',
        ),
        migrations.AddField(
            model_name='empleados',
            name='id',
            field=models.AutoField(default=123, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='tiposact',
            name='id',
            field=models.AutoField(default=123, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='ubicacion',
            name='id',
            field=models.AutoField(default=123, primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='Activity',
        ),
    ]
