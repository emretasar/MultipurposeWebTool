from django import forms
from django.forms import ModelForm
from .models import Task
		

class TaskForm(ModelForm):
    complete = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    deadline = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Task
        fields = ["title", "description", "complete", "deadline"]
