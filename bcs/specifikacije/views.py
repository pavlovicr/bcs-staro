from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView

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

class PostavkaListView(generic.ListView):
    model = Postavka
class PostavkaDetailView(generic.DetailView):
    model = Postavka
class DelaListView(generic.ListView):
    model = Dela
class DelaDetailView(generic.DetailView):
    model = Dela
class SpecifikacijaListView(generic.ListView):
    model = Specifikacija
class SpecifikacijaDetailView(generic.DetailView):
    model = Specifikacija
class KriterijspecifikacijeListView(generic.ListView):
    model = KriterijSpecifikacije
class KriterijspecifikacijeDetailView(generic.DetailView):
    model = KriterijSpecifikacije
