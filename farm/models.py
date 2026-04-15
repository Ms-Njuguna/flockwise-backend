from django.db import models

class Record(models.Model):
    eggs = models.IntegerField()
    income = models.FloatField()
    profit = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)