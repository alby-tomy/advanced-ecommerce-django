from django.http import HttpResponse
from django.shortcuts import render, redirect
from cart.models import Cart, ItemInCart
from django.core.exceptions import ObjectDoesNotExist
from cart.views import _cart_id
import razorpay

def payment_session(request):
    return render(request, 'payment-session.html')

def payment_details(request):
    
    RAZ_KEY = "rzp_test_CBbqyYNgbxjmOz"
    RAZ_SECRET_KEY = "6agQGZiWbUixXmBZBcbeY2Co"
    
         
    client = razorpay.Client(auth=(RAZ_KEY, RAZ_SECRET_KEY))
        
    cart = Cart.objects.get(cart_id = _cart_id)
    order_id = cart.cart_id
    cart_items = ItemInCart.objects.filter(cart=cart, active=True)
        
    total = 0
    for cart_item in cart_items:
        total += (cart_item.product.selling_price * cart_item.quantity)
            
    # convert total into paise for razorpay
    amount = 100000
    order_notes = {'order_id':order_id}
    order_response = client.order.create({
        'amount':amount,
        'currency':"INR",
        'payment_capture':'1',
        'receipt':order_id,
        'partial_payment':False
    })
        
    # create a dictionary containing the payment data for the order
    payment_data = {
        'key':RAZ_KEY,
        'amount':amount,
        'name':'ABC Accessories',
        'currency':"INR",
        'receipt':order_response['receipt'],
        'description':'Payment for the order',
        'prefill':{
            'name':'Alby Tomy',
            'email':'alby.u.tomy@gmail.com',
            'contact':'+916003218505'
        },
        'notes':order_notes
    }
        
    return render(request, 'cart.html',{'payment_data':payment_data})
    
def successful_payment(request):
    # This view will handle the redirect to successful.html after successful payment
    return render(request, 'successful.html')