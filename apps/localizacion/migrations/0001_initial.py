# Generated by Django 4.2.6 on 2023-10-28 20:05

import datetime
from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200, verbose_name='Descripcion')),
                ('descripcion_ampliada', models.TextField(verbose_name='Descricion ampliada')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('usuario_creacion', models.IntegerField(blank=True, help_text='Usuario de creación', null=True, verbose_name='Usuario de creación')),
                ('fecha_alta', models.DateField(default=datetime.date.today, verbose_name='Fecha de alta')),
                ('usuario_alta', models.IntegerField(blank=True, help_text='Usuario de alta', null=True, verbose_name='Usuario de alta')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('usuario_modificacion', models.IntegerField(blank=True, help_text='Usuario de modificación', null=True, verbose_name='Usuario de modificación')),
                ('fecha_baja', models.DateTimeField(blank=True, editable=False, null=True)),
                ('usuario_baja', models.IntegerField(blank=True, help_text='Usuario de baja', null=True, verbose_name='Usuario de baja')),
                ('activo', models.BooleanField(blank=True, default=True, verbose_name='Activo')),
                ('codigo_alfa2', models.CharField(max_length=2, verbose_name='Código Alfa 2')),
                ('codigo_alfa3', models.CharField(max_length=3, verbose_name='Código Alfa 3')),
                ('codigo_numerico', models.IntegerField(verbose_name='Código Numérico')),
            ],
            options={
                'verbose_name': 'País',
                'verbose_name_plural': 'Paises',
                'db_table': 'pais',
                'ordering': ['id'],
                'unique_together': {('descripcion',)},
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200, verbose_name='Descripcion')),
                ('descripcion_ampliada', models.TextField(verbose_name='Descricion ampliada')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('usuario_creacion', models.IntegerField(blank=True, help_text='Usuario de creación', null=True, verbose_name='Usuario de creación')),
                ('fecha_alta', models.DateField(default=datetime.date.today, verbose_name='Fecha de alta')),
                ('usuario_alta', models.IntegerField(blank=True, help_text='Usuario de alta', null=True, verbose_name='Usuario de alta')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('usuario_modificacion', models.IntegerField(blank=True, help_text='Usuario de modificación', null=True, verbose_name='Usuario de modificación')),
                ('fecha_baja', models.DateTimeField(blank=True, editable=False, null=True)),
                ('usuario_baja', models.IntegerField(blank=True, help_text='Usuario de baja', null=True, verbose_name='Usuario de baja')),
                ('activo', models.BooleanField(blank=True, default=True, verbose_name='Activo')),
                ('codigo', models.CharField(max_length=4, verbose_name='Código de Provincia')),
                ('region', models.IntegerField(choices=[(0, 'ESTE'), (1, 'OESTE'), (2, 'NORTE'), (3, 'SUR'), (4, 'NORESTE'), (5, 'SURESTE'), (6, 'NOROESTE'), (7, 'SUROESTE'), (8, 'CENTRO'), (9, 'CENTROESTE'), (10, 'CENTROOESTE'), (11, 'CENTRONORTE'), (12, 'CENTROSUR')], verbose_name='Zona Geográfica:')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='localizacion.pais')),
            ],
            options={
                'verbose_name': 'Provincia',
                'verbose_name_plural': 'Provincias',
                'db_table': 'provincia',
                'ordering': ['id'],
                'unique_together': {('descripcion', 'pais')},
            },
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200, verbose_name='Descripcion')),
                ('descripcion_ampliada', models.TextField(verbose_name='Descricion ampliada')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('usuario_creacion', models.IntegerField(blank=True, help_text='Usuario de creación', null=True, verbose_name='Usuario de creación')),
                ('fecha_alta', models.DateField(default=datetime.date.today, verbose_name='Fecha de alta')),
                ('usuario_alta', models.IntegerField(blank=True, help_text='Usuario de alta', null=True, verbose_name='Usuario de alta')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('usuario_modificacion', models.IntegerField(blank=True, help_text='Usuario de modificación', null=True, verbose_name='Usuario de modificación')),
                ('fecha_baja', models.DateTimeField(blank=True, editable=False, null=True)),
                ('usuario_baja', models.IntegerField(blank=True, help_text='Usuario de baja', null=True, verbose_name='Usuario de baja')),
                ('activo', models.BooleanField(blank=True, default=True, verbose_name='Activo')),
                ('codigo_postal', models.CharField(max_length=6, verbose_name='Código Postal')),
                ('zona', models.IntegerField(choices=[(0, 'Centro'), (1, 'Norte'), (2, 'Sur')], verbose_name='Zona')),
                ('provincia', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='localizacion.provincia')),
            ],
            options={
                'verbose_name': 'Localidad',
                'verbose_name_plural': 'Localidades',
                'db_table': 'ciudad',
                'ordering': ['id'],
                'unique_together': {('descripcion', 'provincia')},
            },
        ),
        migrations.CreateModel(
            name='Barrio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200, verbose_name='Descripcion')),
                ('descripcion_ampliada', models.TextField(verbose_name='Descricion ampliada')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('usuario_creacion', models.IntegerField(blank=True, help_text='Usuario de creación', null=True, verbose_name='Usuario de creación')),
                ('fecha_alta', models.DateField(default=datetime.date.today, verbose_name='Fecha de alta')),
                ('usuario_alta', models.IntegerField(blank=True, help_text='Usuario de alta', null=True, verbose_name='Usuario de alta')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('usuario_modificacion', models.IntegerField(blank=True, help_text='Usuario de modificación', null=True, verbose_name='Usuario de modificación')),
                ('fecha_baja', models.DateTimeField(blank=True, editable=False, null=True)),
                ('usuario_baja', models.IntegerField(blank=True, help_text='Usuario de baja', null=True, verbose_name='Usuario de baja')),
                ('activo', models.BooleanField(blank=True, default=True, verbose_name='Activo')),
                ('zona', models.IntegerField(choices=[(0, 'Urbana'), (1, 'Rural')], verbose_name='Zona')),
                ('localidad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='localizacion.localidad')),
            ],
            options={
                'verbose_name': 'Barrio',
                'verbose_name_plural': 'Barrios',
                'db_table': 'barrio',
                'ordering': ['id'],
                'unique_together': {('descripcion', 'localidad')},
            },
        ),
        migrations.CreateModel(
            name='Calle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200, verbose_name='Descripcion')),
                ('descripcion_ampliada', models.TextField(verbose_name='Descricion ampliada')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('usuario_creacion', models.IntegerField(blank=True, help_text='Usuario de creación', null=True, verbose_name='Usuario de creación')),
                ('fecha_alta', models.DateField(default=datetime.date.today, verbose_name='Fecha de alta')),
                ('usuario_alta', models.IntegerField(blank=True, help_text='Usuario de alta', null=True, verbose_name='Usuario de alta')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('usuario_modificacion', models.IntegerField(blank=True, help_text='Usuario de modificación', null=True, verbose_name='Usuario de modificación')),
                ('fecha_baja', models.DateTimeField(blank=True, editable=False, null=True)),
                ('usuario_baja', models.IntegerField(blank=True, help_text='Usuario de baja', null=True, verbose_name='Usuario de baja')),
                ('activo', models.BooleanField(blank=True, default=True, verbose_name='Activo')),
                ('barrio', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='localidad', chained_model_field='localidad', on_delete=django.db.models.deletion.CASCADE, to='localizacion.barrio', verbose_name='Barrio')),
                ('localidad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='localizacion.localidad', verbose_name='Localidad')),
            ],
            options={
                'verbose_name': 'Calle',
                'verbose_name_plural': 'Calles',
                'db_table': 'calle',
                'ordering': ['id'],
                'unique_together': {('descripcion', 'barrio')},
            },
        ),
    ]
