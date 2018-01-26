from django.contrib import admin
from specifikacije.models import Specifikacija,PodrocjeSpecifikacije,PosebnoDolocilo,SplosnoDolocilo,Dokumentacija

admin.site.register(Specifikacija)
admin.site.register(PodrocjeSpecifikacije)
admin.site.register(PosebnoDolocilo)
admin.site.register(SplosnoDolocilo)
admin.site.register(Dokumentacija)
