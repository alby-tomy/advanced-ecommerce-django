from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def collections(request):
    return render(request,'collections.html')

def loginn(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')