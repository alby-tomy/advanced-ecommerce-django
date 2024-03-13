from django.shortcuts import render, get_object_or_404, render, redirect
from store.models import Product
from .models import Cart, ItemInCart
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.db.models import Q
import razorpay


# Create your views here.


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

@login_required
def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id = _cart_id(request))
        cart.save()
        
    try:
        cart_item = ItemInCart.objects.get(product=product, cart=cart)
        cart_item.quantity +=1
        cart_item.save()
        
    except ItemInCart.DoesNotExist:
        cart_item= ItemInCart.objects.create(product = product, quantity=1, cart=cart)
        cart_item.save()
        
    return redirect('cart:cart-details')



@login_required
def cart_details(request, total=0, counter=0, cart_items=None):
    try:
        cart = Cart.objects.filter(
            Q(cart_id=_cart_id(request)) | Q(user=request.user)).first()

        if not cart:
            cart = Cart.objects.create(cart_id=_cart_id(request), user=request.user)
            cart.save()

        cart_items = ItemInCart.objects.filter(cart=cart, active=True)
        
        total = 0
        for cart_item in cart_items:
            total += (cart_item.product.selling_price * cart_item.quantity)
            counter += cart_item.quantity
            
    except ObjectDoesNotExist:
        pass

    return render(request, 'cart.html', dict(cart_items=cart_items, total=total, counter=counter))



@login_required
def cart_remove(request, product_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    product = get_object_or_404(Product, id=product_id)

    cart_item = ItemInCart.objects.filter(product=product, cart=cart).first()

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart-details')


@login_required
def cart_delete(request, product_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = ItemInCart.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart:cart-details')


@login_required
def logout(request):
    if request.user.is_authenticated:
        # Save cart data if the user was logged in
        cart = Cart.objects.get_or_create(cart_id=_cart_id(request))[0]
        session_cart_items = ItemInCart.objects.filter(cart=cart, active=True)
        for session_cart_item in session_cart_items:
            cart_item, created = ItemInCart.objects.get_or_create(
                product=session_cart_item.product,
                cart=cart,
                defaults={'quantity': session_cart_item.quantity}
            )
            if not created:
                cart_item.quantity += session_cart_item.quantity
                cart_item.save()
        request.session.flush()  # Clear session data

    auth_logout(request)
    return redirect('login')