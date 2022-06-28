from dataclasses import field
from django.forms import ModelForm, Textarea, Select
from .models import News, Answer, User

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['name','author','category', 'description']


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ('user', 'news', 'text')
        widgets = {
            "user": Select(choices=User.objects.all(), attrs={"class": "form-control"}),
            "advert": Select(choices=Answer.objects.all(), attrs={"class": "form-control"}),
            "text": Textarea(attrs={"class": "form-control"})
        }
