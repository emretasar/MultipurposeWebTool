from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate
from django.http import HttpResponseForbidden

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/home")
    else:
        form = RegisterForm()
        return render(response, "register/register.html", {"form":form})
    

def login(response):
    if response.method == "POST":
        form = LoginForm(response.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is None:
                return HttpResponseForbidden()
            else:
                return redirect("/home")
    else:    
        form = LoginForm(response.POST)
        return render(response, "registration/login.html", {"form":form})