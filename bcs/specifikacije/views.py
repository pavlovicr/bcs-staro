from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
#class Karkoli(TemplateView):
#    template_name = "index.html"

from specifikacije.models import Postavka,Specifikacija,Dela,KriterijSpecifikacije


def index(request):

    stej_postavke = Postavka.objects.all().count()
    stej_specifikacije = Specifikacija.objects.all().count()
    stej_dela = Dela.objects.all().count()
    stej_kriterij_specifikacije = KriterijSpecifikacije.objects.all().count()


    return render(request,'specifikacije/index.html',
     context={'stej_postavke':stej_postavke,'stej_specifikacije':stej_specifikacije,
     'stej_dela':stej_dela,'stej_kriterij_specifikacije':stej_kriterij_specifikacije},
        )


class PostavkaList(ListView):
    model = Postavka


class PostavkaDetail(DetailView):
    model = Postavka


class DelaList(ListView):
    model = Dela


class DelaDetail(DetailView):
    model = Dela


class SpecifikacijaList(ListView):
    model = Specifikacija


class SpecifikacijaDetail(DetailView):
    model = Specifikacija


class KriterijSpecifikacijeList(ListView):
    model = KriterijSpecifikacije


class KriterijSpecifikacijeDetail(DetailView):
    model = KriterijSpecifikacije
