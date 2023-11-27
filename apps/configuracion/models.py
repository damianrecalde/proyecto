from django.db import models

# Create your models here.
class Contacto(models.Model):
    # Contacto
    prefijo_celular = models.PositiveSmallIntegerField(
        verbose_name='Prefijo celular', blank=True, null=True)
    celular_nro = models.PositiveIntegerField(
        verbose_name='Nro. celular', blank=True, null=True)
    prefijo = models.PositiveSmallIntegerField(
        verbose_name='Prefijo', blank=True, null=True)
    telefono_nro = models.PositiveIntegerField(
        verbose_name='Nro. teléfono', blank=True, null=True)
    email = models.EmailField(verbose_name='E-mail', blank=True, null=True)

    class Meta:
        abstract = True

class General(models.Model):
    descripcion = models.CharField(max_length=200, verbose_name='Descripcion')
    descripcion_ampliada = models.TextField(verbose_name='Descricion ampliada')

    class Meta:
        abstract = True


class TipoImpuesto(models.Model):
    TIPO = (
        ('Consumidor final', 'Consumidor final'),
        ('Exento', 'Exento'),
        ('Monotributo', 'Mono tributo'),
        ('Responsable inscripto', 'Responsable inscripto'),
    )
    tipoImpuesto = models.CharField(max_length=250, verbose_name='Tipo de impuesto', choices=TIPO, null=False, blank=False)

    #MetaDatos
    class Meta:
        db_table = 'tipoImpuesto'
        verbose_name = 'tipoImpuesto'
        verbose_name_plural = 'Tipo impuestos'
        ordering = ['id']
