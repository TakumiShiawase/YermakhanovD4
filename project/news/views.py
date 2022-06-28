from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from .models import News, Category, Answer, Author
from .forms import NewsForm, AnswerForm
from .filters import NewsFilter
 
 
class NewsList(ListView):
    model = News
    template_name = 'news.html'  
    context_object_name = 'news'  
    paginate_by = 1
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():

            form.save()

        return super().get(request, *args, **kwargs )



class NewsDetail(DetailView):
    template_name = 'news_detail.html'
    queryset = News.objects.all()
    success_url = '/news/'


class NewsSearch(ListView):
    template_name = 'news_search.html'
    queryset = News.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        return context

class NewsCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'news_create.html'
    form_class = NewsForm
    permission_required = ('news.add_news', )


class NewsUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'news_create.html'
    form_class = NewsForm
    permission_required = ('news.change_news', )

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return News.objects.get(pk=id)


class NewsDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'news_delete.html'
    queryset = News.objects.all()
    success_url = '/news/'
    permission_required = ('news.delete_news', )

class AnswerView(ListView):
    queryset = Answer.objects.all()
    template_name = 'answer_list.html'

    def answer_list(request):
        user_name = Author.objects.get(user_name = request.user)
        answer_list = Answer.objects.order_by('-created_answer').filter(author = user_name)
        return answer_list

    

class AnswerDetailView(DetailView):
    template_name = 'answer_detail.html'





class AnswerCreateView(CreateView):
    template_name = 'answer_create.html'
    form_class = AnswerForm
    success_url = '/news/'


class AnswerUpdateView(UpdateView):
    template_name = 'news.html'
    form_class = AnswerForm

class AnswerDeleteView(DeleteView):
    template_name = 'protect/answer_delete.html'
    queryset = Answer.objects.all()
    success_url = '/'
