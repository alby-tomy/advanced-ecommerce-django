from django.shortcuts import render, redirect
from django .contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'index.html')



@login_required(login_url='/login')
def collections(request):
    return render(request,'collections.html')



def loginn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid login')
            return redirect('/login')    
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(username=username).exists():
            messages.info(request,"username already exist")
            return redirect('/register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,"email already taken")
            return redirect('/register')
        
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('/')
    else:
        return render(request,'register.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')