from django.db import models

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ("feed", "Feed"),
        ("transport", "Transport"),
        ("medicine", "Medicine"),
        ("equipment", "Equipment"),
        ("birds", "Birds"),
        ("repairs", "Repairs"),
        ("utilities", "Utilities"),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    amount = models.FloatField()
    description = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)