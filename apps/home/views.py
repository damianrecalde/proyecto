# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.db.models import Count

@login_required(login_url="/ingresar/")
def index(request):
    context = {
        'segment': 'index',
        'titulo':'Informaticasimple.net',
        'pagina_anterior':'Inicio',
        'pagina':'Panel principaL',
        'ip_activa': 'IPS Utilizadas',
        'ip_libre': 'IPS libre',
        'nodos': 'Nodos',
        'clientes': 'Clientes registrados',
        'reportes_titulo': 'Reportes de los registros en el sistema',
        'listado_referentes_titulo': 'Listado de IP registradas en el último mes y su estado actual'
        }

    html_template = loader.get_template('home/dashboard.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/ingresar/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
        
