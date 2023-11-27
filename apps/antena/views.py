from django.shortcuts import render
from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Modo, Producto
from .forms import NuevoProducto
from sweetify.views import SweetifySuccessMixin

class ProductoListView(LoginRequiredMixin, ListView):
	model=Producto
	template_name='producto/list.html'
	login_url='login'
	
	def get_context_data(self, **kwargs):
		context= super().get_context_data(**kwargs)
		context['titulo']='Productos'
		context['titulo_tabla']='Listado de productos'
		context['pantalla_pricipal']='Panel principal'
		context['btn_crear']='Crear producto'
		return context
	

class ProductoCreateView(LoginRequiredMixin, SweetifySuccessMixin, CreateView):
	model= Producto
	form_class=NuevoProducto
	template_name='producto/create.html'
	success_message='El prodicto %(marca)s fue creado correctamente'
	login_url='login'

	def get_context_data(self, **kwargs):
		context= super().get_context_data(*kwargs)
		context['titulo']='Productos'
		context['titulo_seccion']='Crear producto'
		context['titulo_formulario'] = 'Complete el formulario para crear el producto'
		context['pantalla_anterior']='Producto'
		context['leyenda']='Los campos marcados con * son obligatorios'
		context['btn_crear']='Crear'
		context['btn_cancelar']='Cancelar'
		return context