from django.db import models

# FLOCK
class Flock(models.Model):
    TYPE_CHOICES = [
        ("chicks", "Chicks"),
        ("growers", "Growers"),
        ("layers", "Layers"),
    ]

    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    count = models.IntegerField()
    males = models.IntegerField(default=0)
    age_weeks = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


# EGG RECORD
class EggRecord(models.Model):
    eggs_collected = models.IntegerField()
    broken = models.IntegerField(default=0)
    consumed = models.IntegerField(default=0)
    sold = models.IntegerField(default=0)
    price_per_egg = models.FloatField(default=0)
    date = models.DateField(auto_now_add=True)


# BIRD SALES
class BirdSale(models.Model):
    number_sold = models.IntegerField()
    price_per_bird = models.FloatField()
    date = models.DateField(auto_now_add=True)


# EXPENSES
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