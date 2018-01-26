from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

from popisi.models import VrstaDel,Dela,Postavka
from specifikacije.models import Specifikacija,PodrocjeSpecifikacije,SplosnoDolocilo;posebnoDolocilo,Dokumentacija


def index(request):

    stej_postavke = popisi.Postavka.objects.all().count()
    stej_specifikacije = specifikacije.Specifikacija.objects.all().count()
    stej_dela = popisi.Dela.objects.all().count()
    stej_kriterij_specifikacije = specifikacije.PredmetSpecifikacije.objects.all().count()


    return render(request,'osnova/index.html',
     context={'stej_postavke':stej_postavke,'stej_specifikacije':stej_specifikacije,
     'stej_dela':stej_dela,'stej_kriterij_specifikacije':stej_kriterij_specifikacije},
        )
