from django.shortcuts import redirect, render
from django.contrib import messages
from Myapp.forms import CustomUserForm  # Import your CustomUserForm from your app

def Register(request):
    form = CustomUserForm()
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered Successfully! Login to Continue")
            return redirect('/Login')
    context = {'form': form}
    return render(request, 'store/auth/ragister.html', context)

def Login(request):
    return render(request,'store/auth/Login.html')