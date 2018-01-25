from django.db import models
from osnova.models import Osnova
from django.urls import reverse

class SkupinaDolocila(OsnovaPogoji):

    def __str__(self):
        return self.opis

    def get_absolute_url(self):
        return reverse('skupina_dolocila-detail', args=[str(self.id)])


class Dolocilo(OsnovaPogoji):
    skupinadolocila = models.ForeignKey('SkupinaDolocila', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.opis

    def get_absolute_url(self):
        return reverse('pogoj-detail', args=[str(self.id)])

class SkupinaPogoja(OsnovaPogoji):

    def __str__(self):
        return self.opis

    def get_absolute_url(self):
        return reverse('skupina_pogoja-detail', args=[str(self.id)])


class Pogoj(OsnovaPogoji):
    skupinapogoja = models.ForeignKey('SkupinaPogoja', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.opis

    def get_absolute_url(self):
        return reverse('pogoj-detail', args=[str(self.id)])
