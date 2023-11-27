from django import forms
from .models import Cliente

class NuevoCliente(forms.ModelForm):
    class Meta:
        model=Cliente
        fields = [
            'nombre',
            'apellido',
            'empresa',
            'tipo_cliente',
            'tipo_documento',
            'documento_nro',
            'Fecha_nacimiento',
            'observacion',
            'producto',
            'modo',
            'activo'
        ]
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'empresa': 'Empresa a la que pertenece',
            'tipo_cliente': 'Tipo de cliente',
            'tipo_documento': 'Tipo de documento',
            'documento_nro': 'Número de documento',
            'Fecha_nacimiento': 'Fecha de nacimiento',
            'observacion': 'observaciones',
            'producto': 'Tipo de antena',
            'modo': 'Modo de la antena',
            'activo': 'Seleccione si esta actvio el cliente'
        }

        widgets ={
            'nombre': forms.TextInput( attrs={'class':'form-control'}),
            'apellido': forms.TextInput( attrs={'class':'form-control'}),
            'empresa': forms.TextInput( attrs={'class':'form-control'}),
            'tipo_cliente': forms.Select( attrs={'class': 'form-control'}),
            'tipo_documento': forms.TextInput( attrs={'class':'form-control'}),
            'localidad': forms.Select( attrs={'class': 'form-control'}),
            'barrio': forms.Select( attrs={'class': 'form-control'}),
            'calle':forms.Select( attrs={'class': 'form-control'}),
            'calle_nro': forms.TextInput( attrs={'class':'form-control'}),
            'latitud': forms.TextInput( attrs={'class':'form-control'}),
            'longitud': forms.TextInput( attrs={'class':'form-control'}),
            'estado': forms.CheckboxInput( attrs={'class':'custom-control-input', 'id':'customSwitch3'}),
        }