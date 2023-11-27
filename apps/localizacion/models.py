from django.contrib import admin
from django.db import models

from datetime import datetime

from smart_selects.db_fields import ChainedForeignKey

from apps.auditoria.models import Registro
from apps.configuracion.models import General


class Pais(General, Registro):
    codigo_alfa2 = models.CharField(
        'Código Alfa 2'
        ,max_length=2
        ,blank=False
        )
    codigo_alfa3 = models.CharField(
        'Código Alfa 3'
        ,max_length=3
        ,blank= False
        )
    codigo_numerico = models.IntegerField(
        'Código Numérico'
        ,blank=False
        )
    
    #MataDatos
    class Meta:
        db_table = 'pais'
        verbose_name = 'País'
        verbose_name_plural = 'Paises'
        unique_together = [['descripcion']]
        ordering = ['id']
    
    #Métodos
    def __str__(self):
        return "{}".format(
            super().descripcion,
            self.codigo_alfa3
            
        )
    

class Provincia(General, Registro):
    REGIONES = (
        (0, 'ESTE'),
        (1, 'OESTE'),
        (2, 'NORTE'),
        (3, 'SUR'),
        (4, 'NORESTE'),
        (5, 'SURESTE'),
        (6, 'NOROESTE'),
        (7, 'SUROESTE'),
        (8, 'CENTRO'),
        (9, 'CENTROESTE'),
        (10, 'CENTROOESTE'),
        (11, 'CENTRONORTE'),
        (12, 'CENTROSUR')
    )
    pais = models.ForeignKey(
        Pais
        ,on_delete=models.PROTECT
        )
    codigo = models.CharField(
        'Código de Provincia'
        ,max_length=4
        ,blank=False
        )
    region = models.IntegerField(
        'Zona Geográfica:'
        ,choices=REGIONES
        )
    
    #MetaDatos
    class Meta:
        db_table = 'provincia'
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'
        unique_together = [['descripcion', 'pais']]
        ordering = ['id']
    
    #Métodos
    def __str__(self):
        return "{}".format(
            super().descripcion
        )

class Localidad(General, Registro):
    provincia = models.ForeignKey(
        Provincia
        ,on_delete=models.PROTECT
        )
    ZONAS = (
        (0, 'Centro'),
        (1, 'Norte'),
        (2, 'Sur')
    )
    codigo_postal = models.CharField(
        'Código Postal'
        ,max_length=6
        ,blank = False
        )
    zona = models.IntegerField(
        'Zona'
        ,choices=ZONAS
        )

    #MetaDatos
    class Meta:
        db_table = 'ciudad'
        verbose_name = 'Localidad'
        verbose_name_plural = 'Localidades'
        unique_together = [['descripcion', 'provincia']]
        ordering = ['id']

    #Métodos
    def __str__(self):
        return "{}".format(
            super().descripcion,
            self.codigo_postal,
          
        )


class Barrio(General, Registro):
    ZONAS = (
        (0, 'Urbana'),
        (1, 'Rural')
    )
    localidad = models.ForeignKey(
        Localidad
        ,on_delete=models.PROTECT
        )
    zona = models.IntegerField(
        'Zona'
        ,choices=ZONAS
        )
    
    #MetaData
    class Meta:
        db_table = 'barrio'
        verbose_name = 'Barrio'
        verbose_name_plural = 'Barrios'
        unique_together = [['descripcion', 'localidad']]
        ordering = ['id']
        
    #Métodos
    def __str__(self):
        return "{}".format(
            super().descripcion,
        )


class Calle(General, Registro):
    localidad = models.ForeignKey(Localidad, on_delete=models.PROTECT, verbose_name='Localidad')
    barrio=ChainedForeignKey(
        Barrio, 
        chained_field='localidad', 
        chained_model_field='localidad',  
        show_all=False, 
        auto_choose=True, 
        sort=True, 
        verbose_name='Barrio'
        )

    #Métodos
    class Meta:
        verbose_name = 'Calle'
        verbose_name_plural = 'Calles'
        unique_together = [['descripcion', 'barrio']]
        db_table = 'calle'
        ordering = ['id']

    def __str__(self):
        return "{} - {}".format(
            super().descripcion,
            self.localidad,
        )

    
class Ubicacion(models.Model):
    localidad = models.ForeignKey(Localidad, on_delete=models.PROTECT, verbose_name='Localidad', null=True, blank=True)
    barrio = ChainedForeignKey(Barrio, on_delete=models.PROTECT, chained_field='localidad', chained_model_field='localidad',
                               show_all=False, auto_choose=True, sort=True, verbose_name='Barrio', null=True, blank=True)
    calle = ChainedForeignKey(Calle, on_delete=models.PROTECT, chained_field='barrio', chained_model_field='barrio', show_all=False, auto_choose=True,
                              sort=True, related_name='%(app_label)s_%(class)s_calle', verbose_name='Calle', null=True, blank=True)
    calle_nro = models.CharField(
        max_length=20, verbose_name='Calle n°', blank=True, null=True)
    tira_nro = models.CharField(
        max_length=20, verbose_name='Tira', blank=True, null=True)
    piso_nro = models.CharField(
        max_length=20, verbose_name='Piso', blank=True, null=True)
    departamento_nro = models.CharField(
        max_length=20, verbose_name='Departamento', blank=True, null=True)
    casa_nro = models.CharField(
        max_length=20, verbose_name='Casa', blank=True, null=True)
    puerta_nro = models.CharField(
        max_length=20, verbose_name='Puerta', blank=True, null=True)
    seccion_nro = models.CharField(
        max_length=20, verbose_name='Sección', blank=True, null=True)
    parcela_nro=models.CharField(
        max_length=20, verbose_name='Parcela', blank=True, null=True)
    manzana_nro=models.CharField(
        max_length=20, verbose_name='Manzana', blank=True, null=True)
    macizo_nro=models.CharField(
        max_length=20, verbose_name='Macizo', blank=True, null=True)
    lote_nro=models.CharField(
        max_length=20, verbose_name='Lote', blank=True, null=True)
    latitud=models.CharField(
        max_length=20, verbose_name='Latitud', blank=True, null=True)
    longitud=models.CharField(
        max_length=20, verbose_name='Longitud', blank=True, null=True)
    

    class Meta:
        abstract = True

