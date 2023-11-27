from django.db import models
from apps.localizacion.models import Ubicacion
# Create your models here.

class Modo(models.Model):
    TIPO = (
        ('CPE', 'Equipo local cliente'),
        ('AP', 'Acces point'),
        ('RT', 'Router')
    )
    tipoModo = models.CharField(max_length=250, verbose_name='Modo', choices=TIPO, null=False, blank=False)

    #MetaDatos
    class Meta:
        db_table = 'Modo'
        verbose_name = 'tipo de modo'
        verbose_name_plural = 'tipos de modos'
        ordering = ['id']

class Producto(Ubicacion):
    marca= models.CharField(max_length=250, verbose_name='Marca', blank=False, null=False)
    modelo= models.CharField(max_length=250, verbose_name='Modelo', blank=False, null=False)
    producto = models.ForeignKey(Modo, on_delete=models.PROTECT, verbose_name='Modo')
    estado = models.BooleanField(verbose_name='Estado',default=True, null=False, blank=False)

    class Meta:
        db_table= 'Producto'
        verbose_name= 'Producto'
        verbose_name_plural='Productos'
        ordering = ['id']
