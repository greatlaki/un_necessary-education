from django import forms

from .models import *


class AddVideoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['video'].empty_label= 'Видео не выбрано'

    class Meta:
        model = Videos
        fields = ['title', 'video']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
        }
