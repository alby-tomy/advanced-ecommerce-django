from django.shortcuts import render, redirect
from django.contrib import messages
from cart.models import Cart, ItemInCart
from django.core.exceptions import ObjectDoesNotExist
import razorpay


def paymenthandler(request):
    if request.method == 'POST':
        try:
            # retrieve the cart object associated with the current user
            cart = Cart.objects.get(user=request.user)
                        
            cart_items = ItemInCart.objects.filter(cart=cart, active=True)
            
            total = sum(cart_item.product.selling_price * cart_item.quantity for cart_item in cart_items)
                
                
            # Razorpay credential
            RAZOR_KEY_ID = 'rzp_test_CBbqyYNgbxjmOz'
            RAZOR_KEY_SECRET = '6agQGZiWbUixXmBZBcbeY2Co'
            
            # initialize razorpay client
            client = razorpay.Client(
                auth=(RAZOR_KEY_ID,RAZOR_KEY_SECRET)
            )
            
            # create payment order
            order_response = client.order.create({
                'amount':total*100,
                'currency': 'INR',
                'payment_capture':'1'
            })
            
            # extract the order id from the response
            order_id = order_response['id']
            
            # payment data to pass to the template
            payment_data = {
                'key':RAZOR_KEY_ID,
                'total':total*100,
                'order_id':order_id,
            }             
        except ObjectDoesNotExist:
            pass
        
        return render(request, 'cart.html',{'payment_date':payment_data})
    else:
        return redirect('cart:cart_details')