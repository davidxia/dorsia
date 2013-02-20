# -*- coding: utf-8 -*-


from django.conf.urls import patterns, include, url

# Enable admin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'dorsia.views.home', name='home'),
    url(r'^menu$', 'dorsia.views.menu', name='menu'),
    url(r'^reservations$', 'dorsia.views.reservations', name='reservations'),
    url(r'^reviews$', 'dorsia.views.reviews', name='reviews'),
)
