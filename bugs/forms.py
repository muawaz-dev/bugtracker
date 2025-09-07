from django import forms
from . models import Bug
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class BugForm(forms.ModelForm):
    class Meta:
        model=Bug
        fields=['name','bug_type','description','number_of_occurences']
            
