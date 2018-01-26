from django.db import models
from osnova.models import Osnova
from django.urls import reverse
from popisi.models import Dela,VrstaDel,Postavka


class Dokumentacija(Osnova):
    ST='ST'
    SM='SM'
    SL='SL'
    vrsta_dokumenta = (
    (ST, "Standard"),
    (SM, "Smernice"),
    (SL, "Strokovna literatura"),
    )
    vrsta_dokumenta = models.CharField(choices= vrsta_dokumenta,max_length=10, default=ST)

    def __str__(self):
        return self.opis

    def get_absolute_url(self):
        return reverse('dokumentacija-detail', args=[str(self.id)])


class PodrocjeSpecifikacije(Osnova):
    LM='LM'
    PD='PD'
    LI='LI'
    PI='PI'
    VZ='VZ'
    vrsta = (
    (LM, "Lastnosti materialov"),
    (PD, "Pogoji dela"),
    (LI, "Delovni postopki"),
    (PI, "Lastnosti izdelka"),
    (VZ,"Varnostne zahteve"),
    )

    Z='Z'
    P='P'
    S='S'
    osnova = (
    (Z, "Zakonodaja"),
    (P, "Pravila stroke"),
    (S, "Smernice"),
    )
    podrocje = models.CharField(max_length=100)
    podrobnosti = models.CharField(max_length=100)
    vrsta = models.CharField(choices=vrsta,max_length=10, default=LM)
    osnova = models.CharField(choices=osnova,max_length=10, default=P)
    dokumentacija = models.ManyToManyField(Dokumentacija)

    def __str__(self):
        return self.opis

    def get_absolute_url(self):
        return reverse('podrocjespecifikacije-detail', args=[str(self.id)])


class Specifikacija(Osnova):
    podrocje_specifikacije = models.ForeignKey('PodrocjeSpecifikacije', on_delete=models.SET_NULL, null=True)
    postavka = models.ManyToManyField(Postavka)

    def __str__(self):
        return self.opis

    def get_absolute_url(self):
        return reverse('specifikacija-detail', args=[str(self.id)])

class PosebnoDolocilo(Osnova):

    dela = models.ForeignKey('popisi.Dela', on_delete=models.SET_NULL, null=True)
    dokumentacija = models.ManyToManyField(Dokumentacija)

    def __str__(self):
        return self.opis

    def get_absolute_url(self):
        return reverse('posebnodolocilo-detail', args=[str(self.id)])


class SplosnoDolocilo(Osnova):
    vrsta_del = models.ForeignKey('popisi.VrstaDel', on_delete=models.SET_NULL, null=True)
    dokumentacija = models.ManyToManyField(Dokumentacija)

    def __str__(self):
        return self.opis

    def get_absolute_url(self):
        return reverse('splosnodolocilo-detail', args=[str(self.id)])
