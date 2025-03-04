from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list_create, name='product_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('categories/', views.category_list_create, name='category_list_create'),
    path('categories/<int:pk>/', views.category_detail, name='category_detail'),

]
