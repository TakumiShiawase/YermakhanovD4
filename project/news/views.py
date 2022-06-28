from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import News
from .forms import NewsForm
from .filters import NewsFilter
 
 
class NewsList(ListView):
    model = News
    template_name = 'news.html'  
    context_object_name = 'news'  
    paginate_by = 1
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        context['form'] = NewsForm()
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
    model = News
    template_name = 'news_search.html'

class NewsCreate(CreateView):
    template_name = 'news_create.html'
    form_class = NewsForm


class NewsUpdate(UpdateView):
    template_name = 'news_create.html'
    form_class = NewsForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return News.objects.get(pk=id)


class NewsDelete(DeleteView):
    template_name = 'news_delete.html'
    queryset = News.objects.all()
    success_url = '/news/'