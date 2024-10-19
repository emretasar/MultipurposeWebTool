# Generated by Django 4.1 on 2024-10-19 11:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CurrencyAssetEntry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(default=datetime.date.today)),
                (
                    "currency_type",
                    models.CharField(
                        choices=[
                            ("USD", "Dollar"),
                            ("TRY", "Turkish Lira"),
                            ("EUR", "Euro"),
                            ("GLD", "Gold"),
                        ],
                        max_length=3,
                    ),
                ),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "exchange_rate",
                    models.DecimalField(
                        blank=True, decimal_places=4, max_digits=10, null=True
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("owner", models.CharField(default="Not Known", max_length=16)),
            ],
        ),
    ]
