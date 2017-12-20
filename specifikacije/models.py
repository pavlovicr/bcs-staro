from django.db import models
from specifikacije.vaja import Osnova


class Dela(Osnova):
    def __str__(self):
        return self.opis

class Postavka(Osnova):
    enota_mere = models.CharField(max_length=10)
    dela = models.ForeignKey('Dela', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.opis

class OsnovaSpecifikacije(Osnova):
    postavka = models.ManyToManyField(Postavka)

    def __str__(self):
        return self.opis

class Specifikacija(Osnova):
    osnova_specifikacije = models.ForeignKey('OsnovaSpecifikacije', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.opis






