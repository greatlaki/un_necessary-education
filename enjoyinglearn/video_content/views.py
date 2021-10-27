from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from enjoying_people.utils import DataMixin
from video_content.models import *
from video_content.forms import *


class AddVideo(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddVideoForm
    template_name = 'video_content/upload.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавить видео')
        return dict(list(context.items()) + list(c_def.items()))


# def upload_video(request):
#     if request.method == 'POST':
#         title = request.POST['title']
#         video = request.POST['video']
#
#         content = Videos(title=title, video=video)
#         content.save()
#         return redirect('home')
#
#     return render(request, 'video_content/upload.html')


def display(request):
    videos = Videos.objects.all()
    context = {
        'videos': videos,
    }

    return render(request, 'video_content/videos.html', context)
