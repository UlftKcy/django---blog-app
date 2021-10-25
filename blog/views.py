from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from .models import User
from .forms import UserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def home(request):
    return render(request,'blog/home.html')

def register(request):
    form = UserForm()
    
    if request.method == "POST":
        form = UserForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            messages.success(request, "You have been successfully registered")
            login(request,user)
            redirect("home")
    context = {
        "form_user" : form
    }
    return render(request,"blog/register.html",context)


def user_logout(request):
    messages.success(request, "You have been logged out!")
    logout(request)
    return render(request,'blog/logout.html')

def user_login(request):
    form = AuthenticationForm(request,data=request.POST)
    
    if form.is_valid():
        user = form.get_user()
        if user:
            messages.success(request, "You have been logged in successfully")
            login(request, user)
            return redirect('home')
    return render(request, 'blog/login.html', {"form": form})
            
            
