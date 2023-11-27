from django import forms
from .models import Producto

class NuevoProducto(forms.ModelForm):
    class Meta:
        model=Producto
        fields = [
            'marca',
            'modelo',
            'producto',
            'localidad',
            'barrio',
            'calle',
            'calle_nro',
            'latitud',
            'longitud',
            'estado'
        ]
        labels = {
            'marca': 'Marca del producto',
            'modelo': 'Modelo del producto',
            'producto': 'Tipo de producto',
            'localidad': 'Localidad en la que se encuentra',
            'barrio': 'Barrio en donde se encuantra',
            'calle': 'Calle principal donde se encuentra',
            'calle_nro': 'Altura de la calle en la que se encuentra',
            'latitud': 'Latitud en la que se encuentra',
            'longitud': 'Longitud en la que se encuentra',
            'estado': 'Estado'
        }

        widgets ={
            'marca': forms.TextInput( attrs={'class':'form-control'}),
            'modelo': forms.TextInput( attrs={'class':'form-control'}),
            'producto': forms.Select( attrs={'class': 'form-control'}),
            'localidad': forms.Select( attrs={'class': 'form-control'}),
            'barrio': forms.Select( attrs={'class': 'form-control'}),
            'calle':forms.Select( attrs={'class': 'form-control'}),
            'calle_nro': forms.TextInput( attrs={'class':'form-control'}),
            'latitud': forms.TextInput( attrs={'class':'form-control'}),
            'longitud': forms.TextInput( attrs={'class':'form-control'}),
            'estado': forms.CheckboxInput( attrs={'class':'custom-control-input', 'id':'customSwitch3'}),
        }