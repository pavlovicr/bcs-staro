from django.conf.urls import url
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^prvi/$', TemplateView.as_view(template_name ='specifikacije/index.html')),
    url(r'^drugi/$', TemplateView.as_view(template_name ='specifikacije/vaja.html')),
    #url(r'^postavka/$', views.PostavkaListView.as_view(), name='postavka'),
    #url(r'^postavka-detail/(?P<pk>\d+)$', views.PostavkaDetailView.as_view(), name='postavka-detail'),
]
