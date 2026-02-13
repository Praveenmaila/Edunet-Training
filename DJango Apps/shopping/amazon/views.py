from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.
from django.http import HttpResponse
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

def dashboard(request):
    return HttpResponse("Welcome to Amazon dashboard ")
def products(request):
    return HttpResponse("Welcome to the Products")    
def home(request):
    return render(request,"home.html")    