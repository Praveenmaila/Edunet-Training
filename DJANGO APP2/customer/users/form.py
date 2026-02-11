from django import forms
from .models import userForm

class userFormData(forms.ModelForm):
    class Meta:
        model = userForm
        fields = ['name', 'email']