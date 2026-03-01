from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import NoHelpUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    form = NoHelpUserCreationForm()
    print("Creating Form Object")
    if request.method == "POST":
        form = NoHelpUserCreationForm(request.POST)
        print("Form is Post Form")
        if form.is_valid():
            print("Form is valid")
            form.save()
            return redirect("/login")
    return render(request,'register.html',context={"form":form})

def home(request):
    return render(request,'home.html')


def user_login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/welcome")
        else:
            return render(request,'login.html')
    return render(request,'login.html')

@login_required
def welcome(request):
    return render(request,"welcome.html")

def user_logout(request):
    logout(request)
    return redirect("/login")
