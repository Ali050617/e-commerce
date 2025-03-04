from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.order_list_create, name='order_list'),
    path('orders/<int:pk>/', views.order_detail, name='order_detail'),
]
