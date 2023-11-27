from django.db import models
from apps.configuracion.models import General


# Create your models here.
class ClienteTipo(General):
    activo = models.BooleanField(verbose_name='Estado')

    class Meta:
        db_table = 'tipo_cliente'
        verbose_name = 'tipo cliente'
        verbose_name_plural = 'tipos de clientes'
        ordering = ['id']