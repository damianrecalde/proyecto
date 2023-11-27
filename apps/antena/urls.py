from django.urls import path
from apps.antena import views
from apps.antena.views import *

app_name= 'antena'

urlpatterns=[
	path('listado_producto', ProductoListView.as_view(), name='producto_list'),
    path('crear_producto', ProductoCreateView.as_view(), name='producto_create'),
]