from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer

class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer