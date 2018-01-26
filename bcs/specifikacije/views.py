from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

from specifikacije.models import Specifikacija,PodrocjeSpecifikacije,PosebnoDolocilo,SplosnoDolocilo,Dokumentacija


class SpecifikacijaList(ListView):
    model = Specifikacija


class SpecifikacijaDetail(DetailView):
    model = Specifikacija


class PodrocjeSpecifikacijeList(ListView):
    model = PodrocjeSpecifikacije


class PodrocjeSpecifikacijeDetail(DetailView):
    model = PodrocjeSpecifikacije


class PosebnoDolociloList(ListView):
    model = PosebnoDolocilo


class PosebnoDolociloDetail(DetailView):
    model = PosebnoDolocilo


class SplosnoDolociloList(ListView):
    model = SplosnoDolocilo


class SplosnoDolociloDetail(DetailView):
    model = SplosnoDolocilo


class DokumentacijaList(ListView):
    model = Dokumentacija


class DokumentacijaDetail(DetailView):
    model = Dokumentacija
