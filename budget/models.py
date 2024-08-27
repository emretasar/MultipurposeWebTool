from django.db import models
import datetime

class BudgetEntry(models.Model):
    INOUT_CHOICES = [
        ('Income', 'Income'),
        ('Outcome', 'Outcome'),
    ]
    
    inout = models.CharField(max_length=7, choices=INOUT_CHOICES)
    date = models.DateField(default=datetime.date.today)
    amount = models.IntegerField()
    category = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255)
    owner = models.CharField(max_length=16, default="Not Known")
    
    def __str__(self):
        return f"{self.inout} - {self.category} - {self.amount}"
