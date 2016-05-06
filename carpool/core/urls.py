"""carpool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

import core.views

urlpatterns = [
    url(r'^$', core.views.user_login, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', core.views.user_login, name='login'),
    url(r'^logout/$', core.views.user_logout, name='logout'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^pools/$', core.views.pools, name='pools'),
    url(r'^pools/create/$', core.views.create_pool, name='create_pool'),
    url(r'^privacy/', TemplateView.as_view(template_name='privacy.html'), name='privacy'),
    url(r'^terms/', TemplateView.as_view(template_name='terms.html'), name='terms'),
    url(r'^about/', TemplateView.as_view(template_name='about.html'), name='about'),
 ]
