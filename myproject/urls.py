from django.urls import path
from firstapp.views import category_list, category_products

urlpatterns = [
    path('', category_list, name='category_list'),
    path('category/<int:pk>/', category_products, name='category_products'),
]