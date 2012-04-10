from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns("",
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r"^admin/doc/", include("django.contrib.admindocs.urls")),

    url( r"^admin/", include(admin.site.urls)),
    url( r"^$", "dorsianyc.views.home", name = "home" ),
    url( r"^menu$", "dorsianyc.views.menu", name = "menu" ),
    url( r"^reservations$", "dorsianyc.views.reservations", name = "reservations" ),
    url( r"^reviews$", "dorsianyc.views.reviews", name = "reviews" ),

)
