from django.conf.urls import url
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^postavke/$', views.PostavkaList.as_view(), name='postavka-list'),
    url(r'^postavka/(?P<pk>\d+)$', views.PostavkaDetail.as_view(), name='postavka-detail'),
    url(r'^dela/$', views.DelaList.as_view(), name='dela-list'),
    url(r'^dela/(?P<pk>\d+)$', views.DelaDetail.as_view(), name='dela-detail'),
    url(r'^specifikacije/$', views.SpecifikacijaList.as_view(), name='specifikacija-list'),
    url(r'^specifikacija/(?P<pk>\d+)$', views.SpecifikacijaDetail.as_view(), name='specifikacija-detail'),
    url(r'^kriterijspecifikacij/$', views.KriterijSpecifikacijeList.as_view(), name='kriterij_specifikacije-list'),
    url(r'^kriterijspecifikacije/(?P<pk>\d+)$', views.KriterijSpecifikacijeDetail.as_view(), name='kriterij_specifikacije-detail'),
    url(r'^pogoji/$', views.PogojList.as_view(), name='pogoj-list'),
    url(r'^pogoj/(?P<pk>\d+)$', views.PogojDetail.as_view(), name='pogoj-detail'),
    url(r'^dolocila/$', views.DolocilaList.as_view(), name='dolocila-list'),
    url(r'^dolocilo/(?P<pk>\d+)$', views.DolociloDetail.as_view(), name='dolocilo-detail'),
]
