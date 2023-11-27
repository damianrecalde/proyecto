from django.urls import path
from apps.cliente import views
from apps.cliente.views import *


app_name= 'cliente'

urlpatterns=[
    path('listado_cliente', ClienteListView.as_view(), name='cliente_list'),
    path('create_cliente', ClienteCreateView.as_view(), name='cliente_create'),
]