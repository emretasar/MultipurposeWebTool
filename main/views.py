from django.shortcuts import render

# Create your views here.
def home(response):
	return render(response, "main/home.html", {})

def welcome(response):
	return render(response, "main/welcome.html", {})