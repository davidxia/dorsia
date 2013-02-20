# -*- coding: utf-8 -*-


from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.template import RequestContext
from django.template.loader import get_template
from django.shortcuts import render_to_response

from dorsia.models import ReservationForm


def home(request):
    return render_to_response('home.html', {'currentPage': 'home'},
                              context_instance=RequestContext(request))


def menu(request):
    return render_to_response('menu.html', {'currentPage': 'menu'},
                              context_instance=RequestContext(request))


def reservations(request):
    '''Reservations page'''
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()

            # Send email confirmation
            subject = 'Dorsia reservation'
            from_email, to = 'reservation@dorsianyc.com', form.cleaned_data['email']
            txt = get_template('emails/reservation.txt')
            html = get_template('emails/reservation.html')
            data = Context({
                'name': form.cleaned_data['name'],
                'reservation_date': form.cleaned_data['reservationDate'],
                'seating_time': form.cleaned_data['seatingTime'],
                'party_size': form.cleaned_data['partySize'],
            })
            text_content = txt.render(data)
            html_content = html.render(data)
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            # Make main content text/html and attach alternative text only version
            # msg.content_subtype = 'html'
            msg.attach_alternative(html_content, 'text/html')
            msg.send(fail_silently=False)

            form = None
    else:
        form = ReservationForm()

    data = {'currentPage': 'reservations', 'form': form}
    return render_to_response('reservations.html', data,
                              context_instance=RequestContext(request))


def reviews(request):
    return render_to_response('reviews.html', {'currentPage': 'reviews'},
                              context_instance=RequestContext(request))
