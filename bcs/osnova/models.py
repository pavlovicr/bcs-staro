from django.db import models

class OsnovaSpecifikacije(models.Model):
    stevilka = models.IntegerField(null=True)
    koda = models.CharField(max_length=100,null=True)
    opis = models.CharField(max_length=100)

    class Meta:
        abstract = True

class OsnovaPogoji(models.Model):
    stevilka = models.IntegerField(null=True)
    koda = models.CharField(max_length=100,null=True)
    oznaka = models.CharField(max_length=100)
    opis = models.CharField(max_length=100)
    poglavje = models.CharField(max_length=100)
    dokument = models.CharField(max_length=100)

    class Meta:
        abstract = True
