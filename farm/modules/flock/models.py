from django.db import models

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