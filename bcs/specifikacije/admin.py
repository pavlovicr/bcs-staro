from django.contrib import admin
from specifikacije.models import Specifikacija,KlasifikacijaSpecifikacije,PosebnoDolocilo,SplosnoDolocilo,Dokumentacija


#class DokumentacijaAdmin(admin.StackedInline):
#    model = Dokumentacija



class SpecifikacijaAdmin(admin.ModelAdmin):
    fields = ['opis','postavka','klasifikacija_specifikacije',]
#    inline = [ DokumentacijaAdmin, ]






admin.site.register(Specifikacija,SpecifikacijaAdmin)
admin.site.register(KlasifikacijaSpecifikacije)
admin.site.register(PosebnoDolocilo)
admin.site.register(SplosnoDolocilo)
admin.site.register(Dokumentacija)
#admin.site.register(DokumentacijaAdmin)
