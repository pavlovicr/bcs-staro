from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

from popisi.models import VrstaDel,Dela,Postavka


class VrstaDelList(ListView):
    model = VrstaDel


class VrstaDelDetail(DetailView):
    model = VrstaDel


class DelaList(ListView):
    model = Dela


class DelaDetail(DetailView):
    model = Dela


class PostavkaList(ListView):
    model = Postavka


class PostavkaDetail(DetailView):
    model = Postavka
