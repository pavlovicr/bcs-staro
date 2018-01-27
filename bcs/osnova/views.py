from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

from popisi.models import VrstaDel,Dela,Postavka
from specifikacije.models import Specifikacija,PodrocjeSpecifikacije,SplosnoDolocilo,PosebnoDolocilo,Dokumentacija


def index(request):

    stej_postavke = Postavka.objects.all().count()
    stej_specifikacije = Specifikacija.objects.all().count()
    stej_dela = Dela.objects.all().count()
    stej_podrocjespecifikacije = PodrocjeSpecifikacije.objects.all().count()


    return render(request,'osnova/index.html',
     context={'stej_postavke':stej_postavke,'stej_specifikacije':stej_specifikacije,
     'stej_dela':stej_dela,'stej_podrocjespecifikacije':stej_podrocjespecifikacije},
        )
