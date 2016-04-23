import logging

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def user_login(request):
    context = RequestContext(request)

    if request.user.is_authenticated():

        return HttpResponseRedirect(reverse('pools'))

    else:

        return render_to_response('login.html', context)


@login_required
def user_logout(request):
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect(reverse('login'))


@login_required
def pools(request):
    context = RequestContext(request)

    return render_to_response('pools.html', context)

@login_required
def create_pool(request):
    context = RequestContext(request)

    return render_to_response('pools.html', context)
