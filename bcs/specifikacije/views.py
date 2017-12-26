from django.shortcuts import render

from specifikacije.models import Postavka,Specifikacija,Dela,PredmetSpecifikacije


def index(request):

    stej_postavke = Postavka.objects.all().count()
    stej_specifikacije = Specifikacija.objects.all().count()
    stej_dela = Dela.objects.all().count()
    stej_predmet_specifikacije = PredmetSpecifikacije.objects.all().count()


    return render(request,'specifikacije/index.html', context={'stej_postavke':stej_postavke,'stej_specifikacije':stej_specifikacije,'stej_dela':stej_dela,'stej_predmet_specifikacije':stej_predmet_specifikacije},
        )
