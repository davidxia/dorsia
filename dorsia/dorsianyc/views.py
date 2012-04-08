import datetime

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
    """
    Datepicker adapted from http://dl.dropbox.com/u/143355/datepicker/datepicker.html
    """

    partySizes = range( 1, 21 )
    endTime = datetime.datetime.now() + datetime.timedelta( hours = 2 )

    return render_to_response(
        "reservations.html",
        dict( currentPage = "reservations", partySizes = partySizes, endTime = endTime ),
        context_instance = RequestContext( request ) )

def reviews( request ):
    return render_to_response(
        "reviews.html",
        dict( currentPage = "reviews" ),
        context_instance = RequestContext( request ) )
