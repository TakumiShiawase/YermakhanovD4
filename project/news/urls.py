from django.urls import path
from .views import NewsCreate, NewsDelete, NewsList, NewsDetail, NewsSearch, NewsUpdate, AnswerCreateView, AnswerDetailView, AnswerView

 
 
urlpatterns = [
    
    path('', NewsList.as_view()),
    path('<int:pk>', NewsDetail.as_view(), name='news_detail'),
    path('search', NewsSearch.as_view(), name='news_search'),
    path('add/', NewsCreate.as_view(), name='news_create'),
    path('<int:pk>/edit/', NewsUpdate.as_view(), name='news_update'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('answer/', AnswerCreateView.as_view(), name='answer_create'),
    path('answer_detail', AnswerDetailView.as_view(), name='answer_detail'),
    path('answer_list/', AnswerView.as_view(), name='answer_list'),
]