from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('payment-session/', views.payment_session, name='payment-session'),
    path('payment-success/', views.successful_payment, name='successful_payment'),
]
