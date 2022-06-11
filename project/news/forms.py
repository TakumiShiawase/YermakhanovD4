from dataclasses import field
from django.forms import ModelForm
from .models import News

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['name','author','category', 'description']