from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('success/', views.successful_payment, name='successful_payment'),
]
