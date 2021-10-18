from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from .models import *


def index(request):
    if request.POST:
        print(request.POST)

    return HttpResponse('Страница приложения enjoying_people.')


def categories(request, catid):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def upload_video(request):
    if request.method == 'POST':
        title = request.POST['title']
        video = request.POST['video']

        content = Videos(title=title, video=video)
        content.save()
        return redirect('home')

    return render(request, 'upload.html')


def display(request):
    videos = Videos.objects.all()
    context = {
        'videos': videos,
    }

    return render(request, 'videos.html', context)
