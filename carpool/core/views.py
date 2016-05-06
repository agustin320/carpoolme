import logging

import analytics
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect

from core.forms import PoolForm, SearchForm
from core.models import Pool, Dia
from localidad.models import Colonia


@csrf_protect
def user_login(request):
    context = RequestContext(request)

    if request.user.is_authenticated():

        return HttpResponseRedirect(reverse('pools'))

    else:

        return render_to_response('login.html', {'pageType': 'Home Page'}, context)


@login_required
def user_logout(request):

    analytics.track(request.user.pk, 'Logged Out')

    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect(reverse('login'))


@login_required
@csrf_protect
def pools(request):
    context = RequestContext(request)

    resultados = []

    usuario = request.user

    analytics.identify(user_id=usuario.pk,
                       traits={
                           'email': usuario.email,
                           'firstName': usuario.first_name,
                           'lastName': usuario.last_name,
                           'createdAt': usuario.date_joined.isoformat()
                       })

    if request.method == 'POST':

        search_form = SearchForm(request.POST)

        if search_form.is_valid():

            try:
                resultados = Pool.objects.filter(origen=search_form.cleaned_data['origen'],
                                                 destino=search_form.cleaned_data['destino'])


                analytics.track(usuario.pk, 'Busca ruta', {
                    'origen': search_form.cleaned_data['origen'],
                    'destino': search_form.cleaned_data['destino']
                })

            except Exception as e:
                print type(e)
                print e.args
                print e

        else:

            print search_form.errors

    colonias = Colonia.objects.all()

    return render_to_response('pools.html',
                              {'resultados': resultados, 'colonias': colonias, 'pageType': 'Listado Pools'}, context)


@login_required
@csrf_protect
def create_pool(request):
    context = RequestContext(request)

    user = request.user

    if request.method == 'POST':

        pool_form = PoolForm(request.POST, instance=Pool())

        if pool_form.is_valid():

            try:

                pool = Pool.objects.create(creador=user, origen=pool_form.cleaned_data['origen'],
                                           destino=pool_form.cleaned_data['destino']
                                           , tipo=pool_form.cleaned_data['tipo'],
                                           fecha=pool_form.cleaned_data['fecha'])

                dias = pool_form.cleaned_data['dias']

                for dia in dias:
                    pool.dias.add(dia)

                pool.save()

                analytics.track(user.pk, 'Crea ruta', {
                    'origen': pool.origen,
                    'destino': pool.destino
                })

                return HttpResponse("<script>alert('Ruta Creada Exitosamente');window.location.replace('"+request.build_absolute_uri()+"');</script>")

            except Exception as e:
                print type(e)
                print e.args
                print e

        else:
            print pool_form.errors

            return HttpResponse("<script>alert('Hubo un problema a crear la ruta');window.location.replace('"+request.build_absolute_uri()+"');</script>")

    dias = Dia.objects.all()

    colonias = Colonia.objects.all()

    return render_to_response('crear_ruta.html', {'dias': dias, 'colonias': colonias, 'pageType': 'Crear Pool'},
                              context)
