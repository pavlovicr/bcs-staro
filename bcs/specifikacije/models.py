from django.db import models
from django.urls import reverse
#BCS
from osnova.utils import ChoiceEnum
from osnova.models import Osnova
from popisi.models import Dela,VrstaDel,Postavka


class Dokumentacija(Osnova):

    class Zvrst(ChoiceEnum):
        STANDARD = ('Standard')
        PRAVILNIK = ('Pravilnik')
        ZNANOST = ('Znanostvena knjiga')
        PRAKSA = ('Gradbena praksa')
        SMERNICE = ('Smernice')
        PRIPOROCILA = ('Priporocila')

    vrsta_dokumenta = models.CharField(max_length=10, choices=Zvrst.choices(), default=Zvrst.STANDARD)
    komentar = models.TextField()
    dokument = models.CharField(max_length=100)

    def __str__(self):
        return self.opis

    def get_absolute_url(self):
        return reverse('dokumentacija-detail', args=[str(self.id)])


class KlasifikacijaSpecifikacije(Osnova):

    class Osnova(ChoiceEnum):
        ZAKON = ('Zahteve zakonov')
        STROKA = ('Pravila stroke')
        PRAKSA = ('Gradbena praksa')
        SMERNICE = ('Strokovne smernice')
        PRIPOROCILA = ('Priporocila združenj')

    LM='Lastnosti materialov'
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

    Z='Zakonodaja'
    P='Pravila stroke'
    S='Smernice'
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
        return reverse('klasifikacijaspecifikacije-detail', args=[str(self.id)])


class Specifikacija(Osnova):
    klasifikacija_specifikacije = models.ForeignKey('KlasifikacijaSpecifikacije', on_delete=models.SET_NULL, null=True)
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
