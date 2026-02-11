from django.shortcuts import render

# Create your views here.
from .form import userFormData
from .models import userForm

def addUser(request):
    if request.method == "POST":
        form=userFormData(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=userFormData()
    users=userForm.objects.all()
    return render(request, "addUser.html", {"form": form, "users": users})