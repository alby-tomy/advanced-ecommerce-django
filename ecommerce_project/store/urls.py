from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('',views.index, name='home'),
    path('collections',views.collections, name='collections'),
    path('login', views.loginn,name='login'),
    path('register', views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('categories/<slug:category_slug>/', views.products_by_category, name='products_by_category'),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='proDetailName'),
]
