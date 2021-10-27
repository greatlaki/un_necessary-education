from django.urls import path, re_path

from video_content.views import *

urlpatterns = [
    path('upload/', AddVideo.as_view(), name='upload'),
    path('videos/', display, name='videos'),
]