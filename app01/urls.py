from django.contrib import admin
from django.urls import path ,include
from app01 import views

urlpatterns = [
    path('index/',views.index),
    path('customers/',views.customers_index),
    path('sellers/',views.sellers_index),
    path('categories/',views.categories_index),
    path('products/',views.products_index),
    path('brands/',views.brands_index),
    path('brands/store/',views.brands_store),
    path('customers/get/data/',views.customers_get_data),
    path('brands/get/data/',views.brands_get_data),
    path('sellers/get/data/',views.sellers_get_data),
    path('categories/get/data/',views.categories_get_data),
    path('products/get/data/',views.products_get_data),
    path('brands/delete/<int:id>/',views.brands_delete),
    path('categories/store/',views.categories_store),
    path('categories/delete/<int:id>/',views.categories_delete),
    path('products/form/',views.products_form),
    path('products/store/',views.products_store),
    path('customers/store/',views.customers_store),
    path('customers/delete/<int:id>/',views.customers_delete),
    path('products/delete/<int:id>/',views.products_delete),
    path('sellers/store/',views.sellers_store),
    path('sellers/delete/<int:id>/',views.sellers_delete),
    path('brands/edit/<int:id>/',views.brands_edit),
    path('products/edit/<int:id>/',views.products_edit),
    path('products/get/one/',views.products_get_one),
    path('categories/edit/<int:id>/',views.categories_edit),
    path('customers/edit/<int:id>/',views.customers_edit),
    path('sellers/edit/<int:id>/',views.sellers_edit),
    ]