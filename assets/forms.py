from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column

CURRENCY_CHOICES = [
    ('USD', 'Dollar'),
    ('EUR', 'Euro'),
    ('TRY', 'Turkish Lira'),
    ('GOLD', 'Gold'),
]

class CurrencyAssetForm(forms.Form):
    currency_type = forms.ChoiceField(choices=CURRENCY_CHOICES, label="Currency Type")
    exchange_rate = forms.DecimalField(max_digits=10, decimal_places=4, required=False, label="Exchange Rate")
    amount = forms.DecimalField(max_digits=10, decimal_places=2, label="Amount")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('currency_type', css_class='form-group col-md-4 mb-0'),
                Column('exchange_rate', css_class='form-group col-md-4 mb-0'),
                Column('amount', css_class='form-group col-md-4 mb-0'),
            )
        )
