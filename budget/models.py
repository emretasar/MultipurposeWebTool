from django.db import models
import datetime

class BudgetEntry(models.Model):
    INOUT_CHOICES = [
        ('Income', 'Income'),
        ('Outcome', 'Outcome'),
        ('Invest', 'Invest'),
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

class FilterFormModel(models.Model):
    INCOME_OR_EXPENSE_CHOICES = [
        ('Income', 'Income'),
        ('Outcome', 'Outcome'),
        ('Invest', 'Invest'),
        ('Not Selected', 'Not Selected'),
    ]

    MONTH_CHOICES = [
        ('January', 'January'), ('February', 'February'), ('March', 'March'),
        ('April', 'April'), ('May', 'May'), ('June', 'June'),
        ('July', 'July'), ('August', 'August'), ('September', 'September'),
        ('October', 'October'), ('November', 'November'), ('December', 'December'),
        ('Not Selected', 'Not Selected'),
    ]

    CATEGORY_CHOICES = [
        ('Yemek', 'Yemek'),
        ('Tasarruf', 'Tasarruf'),
        ('Fatura', 'Fatura'),
        ('Not Selected', 'Not Selected'),
    ]

    income_or_expense = models.CharField(max_length=12, choices=INCOME_OR_EXPENSE_CHOICES)

    month = models.CharField(max_length=12, choices=MONTH_CHOICES)

    category = models.CharField(max_length=12, choices=CATEGORY_CHOICES)
