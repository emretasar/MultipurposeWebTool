from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Row, Column
from .models import BudgetEntry, FilterFormModel

class BudgetEntryForm(forms.ModelForm):
    inout = forms.Select(choices=BudgetEntry.INOUT_CHOICES)
    amount = forms.NumberInput(attrs={'min': 0})
    date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    category = forms.TextInput(attrs={'placeholder': 'Enter category'}),
    description = forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter a brief description'}),
    
    class Meta:
        model = BudgetEntry
        fields = ['inout', 'amount', 'date', 'category', 'description']


class FilterForm(forms.ModelForm):
    """
    income_or_expense = forms.Select(choices=FilterFormModel.INCOME_OR_EXPENSE_CHOICES)
    month = forms.Select(choices=FilterFormModel.MONTH_CHOICES)
    category = forms.Select(choices=FilterFormModel.CATEGORY_CHOICES)
    """
    class Meta:
        model = FilterFormModel
        fields = ['income_or_expense', 'month', 'category']
    
    def __init__(self, *args, **kwargs):
        super(FilterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = self.helper.layout = Row(
            Column('income_or_expense', css_class='form-group col-md-4 mb-0'),
            Column('month', css_class='form-group col-md-4 mb-0'),
            Column('category', css_class='form-group col-md-4 mb-0'),
        )
        self.helper.add_input(Submit('submit', 'Submit'))