from django.db import models
import datetime 

class CurrencyAssetEntry(models.Model):
    CURRENCY_CHOICES = [
        ('USD', 'Dollar'),
        ('TRY', 'Turkish Lira'),
        ('EUR', 'Euro'),
        ('GLD', 'Gold'),
    ]

    date = models.DateField(default=datetime.date.today)
    currency_type = models.CharField(max_length=3, choices=CURRENCY_CHOICES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, default=1.0)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.CharField(max_length=16, default="Not Known")

    def __str__(self):
        return f"{self.currency_type} - {self.amount}"
