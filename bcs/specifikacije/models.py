from django.db import models
from osnova.models import Osnova
from django.urls import reverse


class Dela(Osnova):
    def __str__(self):
        return self.opis

    def get_absolute_url(self):
        return reverse('dela-detail', args=[str(self.id)])


class Postavka(Osnova):
    enota_mere = models.CharField(max_length=10)
    dela = models.ForeignKey('Dela', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.opis

    def get_absolute_url(self):
        return reverse('postavka-detail', args=[str(self.id)])


class KriterijSpecifikacije(Osnova):
    postavka = models.ManyToManyField(Postavka)

    def __str__(self):
        return self.opis

    def get_absolute_url(self):
        return reverse('kriterij-detail', args=[str(self.id)])


class Specifikacija(Osnova):
    kriterijspecifikacije = models.ForeignKey('KriterijSpecifikacije', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.opis

    def get_absolute_url(self):
        return reverse('specifikacija-detail', args=[str(self.id)])
