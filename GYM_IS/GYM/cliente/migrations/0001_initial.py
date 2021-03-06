# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-07 06:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name=b'Nombre del cliente')),
                ('domicilio', models.TextField(verbose_name=b'direccion del cliente')),
                ('correo', models.CharField(max_length=30, verbose_name=b'Correo')),
                ('telefono', models.CharField(max_length=10, verbose_name=b'Telefono')),
                ('numero_emergencia', models.CharField(blank=True, max_length=10, verbose_name=b'Numero de emergencia')),
                ('fecha_nacimiento', models.DateField(verbose_name=b'Fecha de nacimiento')),
                ('estatura', models.FloatField(verbose_name=b'Estatura')),
                ('peso', models.FloatField(verbose_name=b'Peso')),
                ('alergias', models.IntegerField(blank=True, verbose_name=b'Alergias')),
                ('enfermedades_cronicas', models.IntegerField(blank=True, verbose_name=b'Enfermedades cronicas')),
                ('medicamentos', models.IntegerField(blank=True, verbose_name=b'Nombre del cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Membresia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.IntegerField(verbose_name=b'Tipo de membresia')),
                ('nombre', models.CharField(max_length=12, unique=True, verbose_name=b'Nombre de membresia')),
                ('descripcion', models.TextField(verbose_name=b'Descripcion')),
                ('costo', models.IntegerField(verbose_name=b'Costo')),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, unique=True, verbose_name=b'Nombre de la sucursal')),
                ('direccion', models.TextField(verbose_name=b'Direccion donde se ubica.')),
                ('telefono', models.CharField(max_length=10, verbose_name=b'Telefono')),
                ('hora_apertura', models.DateTimeField(verbose_name=b'Hora de apertura')),
                ('hora_cierre', models.DateTimeField(verbose_name=b'Hora de cierre')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='ID_membresia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.Membresia'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='ID_sucursal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.Sucursal'),
        ),
    ]
