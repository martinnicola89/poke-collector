from django.shortcuts import render
from django.http import HttpResponse
from .models import party


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def poke_index(request):
    return render(request, 'party.html', {'party': party})
