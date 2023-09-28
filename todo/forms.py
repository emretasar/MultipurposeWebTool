from django import forms
from django.forms import ModelForm

from .models import Task


# class TaskForm(ModelForm):
# 	title = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))
# 	description = forms.CharField(required=False, widget= forms.TextInput(attrs={'placeholder':'Describe task...'}))
# 	complete = forms.BooleanField(required=False, widget= forms.CheckboxInput(attrs={'placeholder':'Done...'}))
# 	deadline = forms.DateTimeField(required=False, widget= forms.DateInput(attrs={'placeholder':'Deadline...'}))

# 	class Meta:
# 		model = Task
# 		fields = ["title", "description", "complete", "deadline"]
		
class TaskForm(ModelForm):
    complete = forms.BooleanField(required=False, widget= forms.CheckboxInput())
    deadline = forms.DateField(required=False, widget=forms.DateInput())
    # deadline = forms.DateField(required=False, widget= forms.DateTimeInput())

    class Meta:
        model = Task
        fields = ["title", "description", "complete", "deadline"]
