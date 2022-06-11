from datetime import datetime
from urllib import request
from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product, Category
from .filters import ProductFilter
from .forms import ProductForm
 
 
class ProductsList(ListView):
    model = Product 
    template_name = 'products.html'  
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 1
    

 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        context['form'] = ProductForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():

            form.save()

        return super().get(request, *args, **kwargs )


class ProductDetail(DetailView):
    template_name = 'product_detail.html'  
    queryset = Product.objects.all()
    success_url = '/products/'

class ProductCreateView(CreateView):
    template_name = 'product_create.html'
    form_class = ProductForm
    

class ProductUpdate(UpdateView):
    template_name = 'product_create.html'
    form_class = ProductForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Product.objects.get(pk=id)



class ProductDeleteView(DeleteView):
    template_name = 'product_delete.html'
    queryset = Product.objects.all()
    success_url = '/products/'

