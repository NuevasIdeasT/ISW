# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-07 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Activities', '0002_remove_activity_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='Descripcion',
            field=models.CharField(max_length=100),
        ),
    ]
