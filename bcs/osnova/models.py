from django.db import models

class Osnova(models.Model):
    opis = models.CharField(max_length=100)

    class Meta:
        abstract = True
