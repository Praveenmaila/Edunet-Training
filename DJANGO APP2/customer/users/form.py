from django import forms
from .models import userform
class userFormData(forms.ModelForm):
    class Meta:
        model:userform
        fields:['name','email']