from django.shortcuts import render

# Create your views here.
from .form import userFormData
from .models import userForm

def addUser(request):
    userFormData.request="POST"
    name=request.POST['name']
    email=request.POST['email']