from django.conf.urls import url
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    url(r'^specifikacije/$', views.SpecifikacijaList.as_view(), name='specifikacija-list'),
    url(r'^specifikacija/(?P<pk>\d+)$', views.SpecifikacijaDetail.as_view(), name='specifikacija-detail'),
    url(r'^klasifikacije_specifikacij/$', views.KlasifikacijaSpecifikacijeList.as_view(), name='klasifikacijaspecifikacije-list'),
    url(r'^klasifikacija_specifikacije/(?P<pk>\d+)$', views.KlasifikacijaSpecifikacijeDetail.as_view(), name='klasifikacijaspecifikacije-detail'),
    url(r'^posebna_dolocila/$', views.PosebnoDolociloList.as_view(), name='posebnodolocilo-list'),
    url(r'^posebno_dolocilo/(?P<pk>\d+)$', views.PosebnoDolociloDetail.as_view(), name='posebnodolocilo-detail'),
    url(r'^splosna_dolocila/$', views.SplosnoDolociloList.as_view(), name='splosnodolocilo-list'),
    url(r'^splosno_dolocilo/(?P<pk>\d+)$', views.SplosnoDolociloDetail.as_view(), name='splosnodolocilo-detail'),
    url(r'^dokumentacija/$', views.DokumentacijaList.as_view(), name='dokumentacija-list'),
    url(r'^dokument/(?P<pk>\d+)$', views.DokumentacijaDetail.as_view(), name='dokumentacija-detail'),

]
