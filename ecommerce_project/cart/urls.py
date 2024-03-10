from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('add/<int:product_id>/',views.add_cart, name='add-to-cart'),
    path('cart_details/',views.cart_details, name='cart-details'),
    path('remove/<int:product_id>/',views.cart_remove,name='cart-remove'),
    path('cart_delete/<int:product_id>/',views.cart_delete,name='cart-delete'),
]