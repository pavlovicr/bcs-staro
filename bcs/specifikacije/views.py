from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("SMO NA STRANI SPECIFIKACIJE NA URL INDEX")
