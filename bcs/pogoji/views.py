from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

from pogoji.models import Pogoj,Dolocilo,SkupinaPogoja,SkupinaDolocila


class PogojList(ListView):
    model = Pogoj


class PogojDetail(DetailView):
    model = Pogoj


class SkupinaPogojaList(ListView):
    model = SkupinaPogoja


class SkupinaPogojaDetail(DetailView):
    model = SkupinaPogoja


class DolociloList(ListView):
    model = Dolocilo


class DolociloDetail(DetailView):
    model = Dolocilo


class SkupinaDolocilaList(ListView):
    model = SkupinaDolocila


class SkupinaDolocilaDetail(DetailView):
    model = SkupinaDolocila
