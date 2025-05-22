# produk/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # /produk/
    path('<str:kategori>/', views.item_kategori, name='item_kategori'),  # /produk/elektronik/
    path('<str:kategori>/<int:item_id>/', views.detail_item, name='detail_item'),  # /produk/elektronik/1/
]
