from django import forms
from django.forms import ModelForm
from .models import Note
		

TAG_CHOICES = (
            ("Daily Life", "Daily Life"), 
            ("School", "School"),
            ("Work", "Work"), 
            ("Mingle-Mangle", "Mingle-Mangle"))


class NoteForm(ModelForm):
    
    tag = forms.ChoiceField(choices=TAG_CHOICES)
    note = forms.CharField(widget=forms.Textarea(attrs={'name':'note', 'rows':7, 'cols':5}))
    
    class Meta:
        model = Note
        fields = ["title", "note", "tag"]
