from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    if request.POST:
        print(request.POST)

    return HttpResponse('Страница приложения enjoying_people.')


def categories(request, catid):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")