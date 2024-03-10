from django.shortcuts import get_object_or_404, render, redirect
from django .contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Category, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    return render(request,'index.html')



@login_required(login_url='/login')
def collections(request):
    categories = Category.objects.filter(status=True)
    return render(request, 'collections.html',{'categories':categories})




def category_details(request, category_slug):
    #retrive the category objects based on th eprovided slug
    category = get_object_or_404(Category,slug= category_slug)
    product_list = Product.objects.filter(category=category)
    
    paginator = Paginator(product_list,6)
    page = request.GET.get('page')
    
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
            #If page is not an interget, deliver first page
            products = paginator.page(1)
    except EmptyPage:
        #If page is out of range (e.g 9999), deliver last page of result
        products = paginator.page(paginator.num_pages)
        
    
    return render(request, 'category-details.html',{'category':category, 'products':products})



def product_details(request, category_slug, product_slug):
    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
    return render(request, 'product-details.html', {'product': product})


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