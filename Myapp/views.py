from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from.models import Category,Product
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def Home(request):
    return render(request,"store/index.html")

def collections(request):
    category= Category.objects.filter(status=0)
    context =  {'category':category}
    return render(request, "store/collections.html",context)

def collectionsview(request, slug):
        if(Category.objects.filter(slug=slug,status=0)):
             products =Product.objects.filter(Category__slug=slug)
             category_name = Category.objects.filter(slug=slug).first()
             context = {'products':products,'category_name':category_name}
             return render(request,'store/products/Index.html',context)
        else:
             messages.warning(request,"No Such Category Found")
             return redirect('collections')
        
def productview(request, cate_slug, prod_slug):
    if Category.objects.filter(slug=cate_slug).exists():
        if Product.objects.filter(slug=prod_slug).exists():
            products = Product.objects.filter(slug=prod_slug, status=1).first()
            context = {'products': products}
        else:
            messages.error(request, "No such product found")
            return HttpResponse('No such product found')
    else:
        messages.error(request, "No such category found")
        return redirect('collections')
          
    return render(request, "store/products/view.html", context)

def Ragister(request):
    if request.method == "POST":
        name = request.POST.get('name')  # Updated to match the input field name
        Email = request.POST.get('email')
        pass1 = request.POST.get('password')  # Updated to match the input field name
        pass2 = request.POST.get('ConfirmPassword') 
        
        if not (name and Email and pass1 and pass2):
            return HttpResponse("All fields are required!")
        
        if pass1 != pass2:
            return HttpResponse("Your passwords do not match!")
        
        my_user = User.objects.create_user(name, Email, pass1)
        my_user.save()
        return redirect('Login')

    return render(request, "store/ragister.html")

def Login(request):
    if request.user.is_authenticated:
        messages.warning(request, "You have already logged in.")    
        return redirect("home")
    else: 
        if request.method == 'POST':
            username = request.POST.get('name') 
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('home')
            else:
                messages.error(request, 'Username or password is incorrect.')
                return redirect('Cantlogin')
    
        return render(request, 'store/Login.html')

def Logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged out Successfully")
    return redirect("home")
    