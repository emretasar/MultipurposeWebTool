from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import BudgetEntry

class BudgetEntryForm(forms.ModelForm):
    inout = forms.Select(choices=BudgetEntry.INOUT_CHOICES)
    amount = forms.NumberInput(attrs={'min': 0})
    date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    category = forms.TextInput(attrs={'placeholder': 'Enter category'}),
    description = forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter a brief description'}),
    
    class Meta:
        model = BudgetEntry
        fields = ['inout', 'amount', 'date', 'category', 'description']

