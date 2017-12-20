from django.db import models

class Osnova(models.Model):
    stevilka = models.IntegerField(null=True)
    koda = models.CharField(max_length=100,null=True)
    opis = models.CharField(max_length=100)

    class Meta:
        abstract = True
