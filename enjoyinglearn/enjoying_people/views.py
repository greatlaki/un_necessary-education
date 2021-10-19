from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from .models import *


def index(request):
    return render(request, 'enjoying_people/index.html')


def about(request):
    return render(request, 'enjoying_people/about.html')


def categories(request, catid):
    if request.POST:
        print(request.POST)

    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


