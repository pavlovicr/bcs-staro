from django.contrib import admin
from specifikacije.models import Dela,Postavka,Specifikacija,OsnovaSpecifikacije

class DelaAdmin(admin.ModelAdmin):
    pass

class PostavkaAdmin(admin.ModelAdmin):
    pass

class SpecifikacijaAdmin(admin.ModelAdmin):
    pass

class OsnovaSpecifikacijeAdmin(admin.ModelAdmin):
    pass







admin.site.register(Dela,DelaAdmin)
admin.site.register(Postavka,PostavkaAdmin)
admin.site.register(Specifikacija,SpecifikacijaAdmin)
admin.site.register(OsnovaSpecifikacije,OsnovaSpecifikacijeAdmin)
