from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView
#from django.views.generic import TemplateView

#class Karkoli(TemplateView):
#    template_name = "index.html"

from specifikacije.models import Postavka,Specifikacija,Dela,PredmetSpecifikacije


def index(request):

    stej_postavke = Postavka.objects.all().count()
    stej_specifikacije = Specifikacija.objects.all().count()
    stej_dela = Dela.objects.all().count()
    stej_predmet_specifikacije = PredmetSpecifikacije.objects.all().count()


    return render(request,'specifikacije/index.html', context={'stej_postavke':stej_postavke,'stej_specifikacije':stej_specifikacije,'stej_dela':stej_dela,'stej_predmet_specifikacije':stej_predmet_specifikacije},
        )

#class PostavkaListView(generic.ListView):
#    model = Postavka

#class PostavkaDetailView(DetailView):

#    context_object_name = 'opis'
#    queryset = Postavka.objects.all()
