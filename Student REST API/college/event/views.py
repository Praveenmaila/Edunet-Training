from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer


@method_decorator(csrf_exempt, name='dispatch')
class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

def dashboard(request):
    return render(request,'dashboard.html')