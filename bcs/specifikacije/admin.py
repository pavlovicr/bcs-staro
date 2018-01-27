from django.contrib import admin
from specifikacije.models import Specifikacija,PodrocjeSpecifikacije,PosebnoDolocilo,SplosnoDolocilo,Dokumentacija

class SpecifikacijaAdmin(admin.ModelAdmin):
    fields = ['opis','postavka']
    #inline = []



admin.site.register(Specifikacija,SpecifikacijaAdmin)
admin.site.register(PodrocjeSpecifikacije)
admin.site.register(PosebnoDolocilo)
admin.site.register(SplosnoDolocilo)
admin.site.register(Dokumentacija)
