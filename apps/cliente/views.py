from django.shortcuts import render
from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from .models import Cliente
from sweetify.views import SweetifySuccessMixin
from .forms import NuevoCliente


class ClienteListView(LoginRequiredMixin, ListView):
    model=Cliente
    template_name='cliente/list.html'
    login_url='login'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['titulo']='Clientes'
        context['titulo_tabla']='Listado de clientes'
        context['pantalla_principal']='Panel principal'
        context['btn_crear']='Crear cliente'
        return context



class ClienteCreateView(LoginRequiredMixin, SweetifySuccessMixin, CreateView):
    model = Cliente
    form_class = NuevoCliente
    template_name='cliente/create.html'
    login_url='login'
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(*kwargs)
        context['titulo']='Cliente'
        context['titulo_seccion']='Crear cliente'
        context['titulo_formulario']='Complete el formulario para crear el cliente'
        context['pantalla_anterior']='Cliente'
        context['leyenda']='Los campos marcados con * son obligatorios'
        context['btn_crear']='Crear'
        context['btn_cancelar']='Cancelar'
        return context