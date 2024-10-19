from django import forms
from decimal import Decimal
from .models import CurrencyAssetEntry

class CurrencyAssetForm(forms.ModelForm):
    date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    currency_type = forms.Select(choices=CurrencyAssetEntry.CURRENCY_CHOICES)
    amount = forms.DecimalField(max_digits=12, decimal_places=2)
    exchange_rate = forms.DecimalField(max_digits=10, decimal_places=4, initial = Decimal('1.00'))

    class Meta:
        model = CurrencyAssetEntry
        fields = ['date', 'currency_type', 'amount', 'exchange_rate']
