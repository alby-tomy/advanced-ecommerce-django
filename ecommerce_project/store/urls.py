from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('',views.index, name='home'),
    path('collections/', views.collections, name='collections'),
    path('login/', views.loginn, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('collection/<slug:category_slug>/', views.category_details, name='category_details'),
    path('collection/<slug:category_slug>/<slug:product_slug>/', views.product_details, name='product_details'),
    # path('product', views.product, name='product'),
]
