from django.conf.urls import url
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    url(r'^pogoji/$', views.PogojList.as_view(), name='pogoj-list'),
    url(r'^pogoj/(?P<pk>\d+)$', views.PogojDetail.as_view(), name='pogoj-detail'),
    url(r'^dolocila/$', views.DolocilaList.as_view(), name='dolocila-list'),
    url(r'^dolocilo/(?P<pk>\d+)$', views.DolociloDetail.as_view(), name='dolocilo-detail'),
    url(r'^skupina_pogoji/$', views.SkupinaPogojList.as_view(), name='skupina_pogoj-list'),
    url(r'^skupina_pogoj/(?P<pk>\d+)$', views.SkupinaPogojDetail.as_view(), name='skupina_pogoj-detail'),
    url(r'^skupina_dolocila/$', views.SkupinaDolocilaList.as_view(), name='skupina_dolocila-list'),
    url(r'^skupina_dolocilo/(?P<pk>\d+)$', views.DolociloDetail.as_view(), name='skupina_dolocilo-detail'),







]
