from django.db import models

class EggRecord(models.Model):
    eggs_collected = models.IntegerField()
    broken = models.IntegerField(default=0)
    consumed = models.IntegerField(default=0)
    sold = models.IntegerField(default=0)
    price_per_egg = models.FloatField(default=0)
    date = models.DateField(auto_now_add=True)


class BirdSale(models.Model):
    number_sold = models.IntegerField()
    price_per_bird = models.FloatField()
    date = models.DateField(auto_now_add=True)