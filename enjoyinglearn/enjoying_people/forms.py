from django import forms
from .models import *


class AddPostForm(forms.ModelForm):
    class Meta:
        model = People
        fields = '__all__'