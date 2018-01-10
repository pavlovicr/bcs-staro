from django.db import models
from osnova.models import Osnova


class Dela(Osnova):
    def __str__(self):
        return self.opis

    def get_absolute_url(self):
#       """
#        Vrne url za Dela.
#        """
        return reverse('dela-detail', args=[str(self.id)])



class Postavka(Osnova):
    enota_mere = models.CharField(max_length=10)
    dela = models.ForeignKey('Dela', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.opis

    def get_absolute_url(self):
        """
        Vrne url za Postavka.
        """
        return reverse('postavka-detail', args=[str(self.id)])


class PredmetSpecifikacije(Osnova):
    postavka = models.ManyToManyField(Postavka)

    def __str__(self):
        return self.opis

    def get_absolute_url(self):
        """
        Vrne url za Predmet specifikacije.
        """
        return reverse('predmet-detail', args=[str(self.id)])



class Specifikacija(Osnova):
    predmet = models.ForeignKey('PredmetSpecifikacije', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.opis

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('specifikacija-detail', args=[str(self.id)])
