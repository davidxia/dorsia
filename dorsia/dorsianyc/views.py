from datetime import datetime

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

from dorsianyc.models import Reservation, ReservationForm


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
    Reservations page
    """

    if request.method == "POST":
        form = ReservationForm( request.POST )
        if form.is_valid():
            form.save()
            form = None
    else:
        form = ReservationForm()


    data = dict( currentPage = "reservations", form = form )

    return render_to_response(
        "reservations.html",
        data,
        context_instance = RequestContext( request ) )


def reviews( request ):
    return render_to_response(
        "reviews.html",
        dict( currentPage = "reviews" ),
        context_instance = RequestContext( request ) )
