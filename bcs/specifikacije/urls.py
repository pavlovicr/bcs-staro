from django.conf.urls import url
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^prvi/$', TemplateView.as_view(template_name ='specifikacije/index.html')),

    url(r'^postavke/$', views.PostavkaListView.as_view(), name='ratata'),
    url(r'^postavka/(?P<pk>\d+)$', views.PostavkaDetailView.as_view(), name='postavka-detail'),
    url(r'^dela/$', views.DelaListView.as_view(), name='rompompom'),
    url(r'^dela/(?P<pk>\d+)$', views.DelaDetailView.as_view(), name='dela-detail'),
    url(r'^specifikacije/$', views.SpecifikacijaListView.as_view(), name='horuk'),
    url(r'^specifikacija/(?P<pk>\d+)$', views.SpecifikacijaDetailView.as_view(), name='specifikacija-detail'),
    url(r'^kriterijspecifikacij/$', views.KriterijspecifikacijeListView.as_view(), name='hojladri'),
    url(r'^kriterijspecifikacije/(?P<pk>\d+)$', views.KriterijspecifikacijeDetailView.as_view(), name='kriterij-detail'),



]
