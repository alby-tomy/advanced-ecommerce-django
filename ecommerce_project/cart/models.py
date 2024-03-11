from django.db import models

# Create your models here.
from store.models import Product
from django.contrib.auth.models import User

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    cart_id = models.CharField(max_length=255, blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Cart'
        ordering = ['date_added']

    def __str__(self):
        return '{}'.format(self.cart_id)
    
class ItemInCart(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'ItemInCart'
        
    def subTotal(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return '{}'.format(self.product)