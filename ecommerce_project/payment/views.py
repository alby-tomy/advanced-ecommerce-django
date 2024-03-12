from django.shortcuts import render, redirect
from cart.models import Cart, ItemInCart
from django.core.exceptions import ObjectDoesNotExist
import razorpay
import uuid
import time

def generate_order_id():
    # Generate a random UUID
    unique_id = uuid.uuid4()
    
    # Get the current timestamp (in milliseconds)
    timestamp_ms = int(time.time() * 1000)
    
    # Combine the timestamp and UUID to create the order ID
    order_id = f"{timestamp_ms}-{unique_id}"
    
    return order_id

def paymenthandler(request):
    if request.method == 'POST':
        try:
            # retrieve the cart object associated with the current user
            cart = Cart.objects.get(user=request.user)
                        
            cart_items = ItemInCart.objects.filter(cart=cart, active=True)
            
            total = sum(cart_item.product.selling_price * cart_item.quantity for cart_item in cart_items)
                
                
            
            
            # initialize razorpay client
            client = razorpay.Client(
                auth=("rzp_test_CBbqyYNgbxjmOz", "6agQGZiWbUixXmBZBcbeY2Co")
            )
            
            # Create a unique order_id
            order_id = generate_order_id()
            
            # Create payment order
            order_response = client.order.create({
                'amount': (total * 100),  # Amount in paise
                'currency': 'INR',
                'payment_capture': '1',
                'receipt': str(order_id),
                'partial_payment': False,
            })
            
            # Extract the order ID from the response
            razorpay_order_id = order_response['id']
            
            # Payment data to pass to the template
            payment_data = {
                'total': int(total * 100),
                'order_id': razorpay_order_id,
            }
            
            print(payment_data.key)             
        except ObjectDoesNotExist:
            pass
        
        return render(request, 'cart.html', {'payment_data': payment_data})
    else:
        return redirect('cart:cart_details')

def successful_payment(request):
    # This view will handle the redirect to successful.html after successful payment
    return render(request, 'successful.html')