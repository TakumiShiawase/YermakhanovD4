from django.urls import path
from .views import ProductsList, ProductDetail, ProductCreateView, ProductUpdate, ProductDeleteView
 
 
urlpatterns = [
    
    path('', ProductsList.as_view()),
    path('<int:pk>', ProductDetail.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('update/<int:pk>', ProductUpdate.as_view(), name='product_update'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete')
]