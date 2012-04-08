from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def home( request ):
    return render_to_response(
        "home.html",
        dict( currentPage = "home" ),
        context_instance = RequestContext( request ) )

def menu( request ):
    return render_to_response(
        "menu.html",
        dict( currentPage = "menu" ),
        context_instance = RequestContext( request ) )

def reservations( request ):
    return render_to_response(
        "reservations.html",
        dict( currentPage = "reservations" ),
        context_instance = RequestContext( request ) )

