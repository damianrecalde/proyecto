from django.db import models
from apps.configuracion.models import Contacto, TipoImpuesto
from apps.localizacion.models import Ubicacion
from apps.clienteTipo.models import ClienteTipo
from apps.antena.models import Producto, Modo
# Create your models here.

class Cliente(Ubicacion, Contacto, TipoImpuesto):
    nombre = models.CharField(max_length=255, verbose_name='Nombre', blank=True, null=True)
    apellido = models.CharField(max_length=255, verbose_name='Apellido', blank=False, null=True)
    empresa = models.CharField(max_length=255, verbose_name='Empresa', blank=True, null=True)
    tipo_cliente = models.ForeignKey(ClienteTipo, on_delete=models.PROTECT, verbose_name='Tipo de cliente')
    tipo_documento = models.CharField(max_length=10, verbose_name='Tipo de documento', blank=True, null=True)
    documento_nro = models.CharField(max_length=12, verbose_name='Numero de documento', blank=True, null=True)
    Fecha_nacimiento = models.DateField(verbose_name='Fecha de nacimiento', blank=True, null=True)
    observacion = models.TextField(blank=True, null=True, verbose_name='Observacion')
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT, verbose_name='Producto')
    modo = models.ForeignKey(Modo, on_delete=models.PROTECT, verbose_name='Modo')
    activo = models.BooleanField(verbose_name='Estado cliente')

    class Meta:
        db_table= 'cliente'
        verbose_name= 'Cliente'
        verbose_name_plural= 'Clientes'
        #unique_together = [['documento_nro']]
        ordering = ['id']

     #Métodos
    def __str__(self):
        return "{}, {}".format(
            self.nombre,
            self.apellido
        )
        
        
class IpAsignada(models.Model):
    numeroIp= models.CharField(max_length=15, verbose_name="Ip", blank=True, null="True")
    estado = models.BooleanField(verbose_name='Estado',default=True, null=False, blank=False)
    
    class Meta:
        db_table= 'ipAsignada'
        verbose_name= 'ipAsignada'
        verbose_name_plural= 'ipAsignadas'
        
        

class IpAsignadaCliente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, verbose_name='Cliente')
    ipAsignada = models.ForeignKey(IpAsignada, on_delete=models.PROTECT, verbose_name='Ip asignada')
    #MetaDatos
    class Meta:
        db_table = 'ip_asignada_cliente'
        verbose_name = 'Ip asignada a cliente'
        verbose_name_plural = 'Ip asignada a cliente'
        # unique_together = [['descripcion']]
        ordering = ['id']
    
    #Métodos
    def __str__(self):
        return "{}".format(
            self.cliente,
        )
