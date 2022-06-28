from tkinter import CASCADE
from django.db import models
from django.core.validators import MinValueValidator
from django.db import models
from asyncio.proactor_events import _ProactorBaseWritePipeTransport
from django.contrib.auth.models import User
from django.db.models import Sum


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    ratingAuthor = models.SmallIntegerField(default=0)


    def update_rating(self):
        postRat = self.post_set.all().aggregate(postRating=Sum('rating'))
        pRat = 0
        pRat += postRat.get('postRating')

        commentRat = self.authorUser.comment_set.all().aggregate(commentRating=Sum('rating'))
        cRat = 0
        cRat += commentRat.get('commentRating')

        self.ratingAuthor = pRat * 3 + cRat
        self.save() 
  
class News(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=50,
        unique=True,
    )
    datetime = models.DateTimeField(auto_now_add=True)

    description = models.TextField()

    
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='news', 
    )

    

 
    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'

    def get_absolute_url(self):
        return f'/news/{self.id}'
 
 

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  
 
    def __str__(self):
        return f'{self.name.title()}'

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='replies')
    text = models.TextField()
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    taken = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'Answer by {self.user} on {self.news}'

