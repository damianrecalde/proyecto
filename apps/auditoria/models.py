import datetime
from django.db import models

# Create your models here.
class Registro(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True, blank=True)
    usuario_creacion = models.IntegerField(verbose_name='Usuario de creación', help_text='Usuario de creación', null=True, blank=True)
    fecha_alta = models.DateField(default=datetime.date.today, verbose_name='Fecha de alta')
    usuario_alta = models.IntegerField(verbose_name='Usuario de alta', help_text='Usuario de alta', null=True, blank=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    usuario_modificacion = models.IntegerField(verbose_name='Usuario de modificación', help_text='Usuario de modificación', null=True, blank=True)
    fecha_baja = models.DateTimeField(editable=False, blank=True, null=True)
    usuario_baja = models.IntegerField(verbose_name='Usuario de baja', help_text='Usuario de baja', null=True, blank=True)
    activo = models.BooleanField(default=True, verbose_name='Activo', blank=True)

    class Meta:
        abstract = True


class Operacion(models.TextChoices):
    # Operacion, clase para determinar las operaciones para el modelo auditoria
    ACCESO = 'ACCESO', 'Acceso'
    CREACION = 'CREACION', 'Creación'
    MODIFICACION = 'MODIFICACION', 'Modificación'
    ELIMINACION = 'ELIMINACION', 'Eliminación'


class Respuesta(models.IntegerChoices):
    # Respuesta, clase para determinar las respuestas para el modelo auditoria
    OK = 200
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500


class Auditoria(models.Model):
    usuario = models.CharField(max_length=50, verbose_name='Usuario', blank=True, null=True)
    operacion = models.CharField(max_length=15, verbose_name='Operación', choices=Operacion.choices, null=True, blank=True)
    respuesta = models.IntegerField(verbose_name='Respuesta', choices=Respuesta.choices, null=True, blank=True)
    observacion = models.TextField(verbose_name='Observación', blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.usuario, self.operacion)

    class Meta:
        verbose_name = 'Auditoria'
        verbose_name_plural = 'Auditorias'
        db_table = 'auditoria'
        ordering = ['id']

