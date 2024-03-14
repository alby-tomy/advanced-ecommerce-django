from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .models import PaymentAddress

def payment_session(request):
    return render(request, 'payment-session.html')


def paymnet_address(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        district = request.POST['district']
        state = request.POST['state']
        pincode = request.POST['pincode']
        mobile_number = request.POST['mobile_number']
        email = request.POST['email']
        additional_info = request.POST['additional_info']
        remember_address = request.POST['remember_address']
        
        if PaymentAddress.onjects.filter(mobile_number = mobile_number).exists():
            messages.info(request, "mobile  number already exists")
            return redirect('/paymnet-session')
        if PaymentAddress.objects.filter(email=email):
            messages.info(request,"email is already taken")
            return redirect('/paymnet-session')
        
        payment_address = PaymentAddress.objects.create(
                first_name=first_name,
                last_namee=last_name,
                address = address,
                district = district,
                state = state,
                pincode = pincode,
                email = email,
                additional_info = additional_info,
                remember_address = remember_address
        )
        payment_address.save()
        return redirect('payment:payment-session')
    else:
        return render(request,'paymnet:payment-session')
            

    
def payment_details(request):
    
    RAZ_KEY = "rzp_test_CBbqyYNgbxjmOz"
    RAZ_SECRET_KEY = "6agQGZiWbUixXmBZBcbeY2Co"
    return render(request, 'cart.html')
    
def successful_payment(request):
    # This view will handle the redirect to successful.html after successful payment
    return render(request, 'successful.html')