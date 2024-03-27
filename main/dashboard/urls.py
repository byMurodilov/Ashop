from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index),
    # ------CATEGORY------------
    path('category-list', views.category_list, name='category_list'),
    path('category-create', views.category_create, name='category_create'),
    path('category-update/<int:id>/', views.category_update, name='category_update'),
    path('category-delete/<int:id>/', views.category_delete, name='category_delete'),
    # ------PRODUCT------------
    path('product-list', views.product_list, name='product_list'),
    path('product-create', views.product_create, name='product_create'),
    path('product-detail/<int:id>/', views.product_detail, name='product_detail'),
    path('product-update/<int:id>/', views.product_update, name='product_update'),
    path('product-delete/<int:id>/', views.product_delete, name='product_delete'),
]