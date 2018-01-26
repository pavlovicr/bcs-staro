from django.db import models
from osnova.models import Osnova
from django.urls import reverse


class VrstaDel(Osnova):
    GR='GR'
    OB='OB'
    skupina_del = (
    (GR, "Gradbena dela"),
    (OB, "Obrtniška dela"),
    )
    skupina_del = models.CharField(choices = skupina_del, max_length=10, default=GR)

    def __str__(self):
        return self.opis

    def get_absolute_url(self):
        return reverse('vrstadel-detail', args=[str(self.id)])


class Dela(Osnova):
    vrsta_del = models.ForeignKey('VrstaDel', on_delete=models.SET_NULL, null=True)
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
