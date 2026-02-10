from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse

def dashboard(request):
    return HttpResponse("Welcome to Amazon dashboard ")
def products(request):
    return HttpResponse("Welcome to the Products")    
def home(request):
    return render(request,"home.html")    