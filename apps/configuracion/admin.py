from django.contrib import admin

from apps.configuracion.models import TipoImpuesto

# Register your models here.
class TipoImpuestoAdmin(admin.ModelAdmin):
  display = (
    'tipoImpuesto'
  )
  
admin.site.register(TipoImpuesto,TipoImpuestoAdmin)