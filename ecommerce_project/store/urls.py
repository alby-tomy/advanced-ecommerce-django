from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('',views.index, name='home'),
    path('collections',views.collections, name='collections'),
    path('login', views.loginn,name='login'),
    path('register', views.register,name='register'),
]
