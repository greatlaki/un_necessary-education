from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = [{"title": "О сайте", "url_name": 'about'},
        {"title": "Добавить статью", "url_name": 'add_page'},
        {"title": "Обратная связь", "url_name": 'contact'},
        {"title": "Войти", "url_name": 'login'},
]


def index(request):
    posts = People.objects.all()
    return render(request, 'enjoying_people/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})


def about(request):
    return render(request, 'enjoying_people/about.html', {'menu': menu, 'title': 'О сайте'})


def add_page(request):
    return HttpResponse('Добавление статьи')


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


