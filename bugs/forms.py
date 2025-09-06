from django import forms
from . models import Bug

class BugForm(forms.ModelForm):
    class Meta:
        model=Bug
        fields=['name','bug_type','description','number_of_occurences']
            
