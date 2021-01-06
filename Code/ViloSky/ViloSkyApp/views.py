from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.conf import settings

# Create your views here.
def index(request):
    return render(request, 'index.html', {}) 

def login(request):
    return render(request, 'login.html', {}) 

def register(request):
    return render(request, 'register.html', {}) 

def dashboard(request):
    return render(request, 'dashboard.html', {}) 
    
def mydetails(request):
    return render(request, 'mydetails.html', {}) 