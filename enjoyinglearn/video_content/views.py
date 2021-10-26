from django.shortcuts import redirect, render

from video_content.models import *


def upload_video(request):
    if request.method == 'POST':
        title = request.POST['title']
        video = request.POST['video']

        content = Videos(title=title, video=video)
        content.save()
        return redirect('home')

    return render(request, 'video_content/upload.html')


def display(request):
    videos = Videos.objects.all()
    context = {
        'videos': videos,
    }

    return render(request, 'video_content/videos.html', context)
