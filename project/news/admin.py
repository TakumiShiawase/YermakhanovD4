from django.contrib import admin
from .models import Author, Category, News
 
 
admin.site.register(Category)
admin.site.register(News)
admin.site.register(Author)