from django.db import models
from cart.models import ItemInCart
from django.test import RequestFactory

class PaymentAddress(models.Model):
    
    amount_request = RequestFactory().get('cart:cart-details')
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    mobile_number = models.CharField(max_length=15)
    email = models.CharField(max_length=50, default=False)
    additional_info = models.TextField()
    remember_address = models.BooleanField(default=False)
    