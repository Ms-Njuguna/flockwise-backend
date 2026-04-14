from django.db import models

class FlockGroup(models.Model):
    GROUP_TYPES = [
        ('chicks', 'Chicks'),
        ('growers', 'Growers'),
        ('layers', 'Layers'),
    ]

    name = models.CharField(max_length=100)
    group_type = models.CharField(max_length=20, choices=GROUP_TYPES)
    bird_count = models.IntegerField()
    age_weeks = models.IntegerField()

    def __str__(self):
        return self.name


class DailyRecord(models.Model):
    flock = models.ForeignKey(FlockGroup, on_delete=models.CASCADE)
    eggs_collected = models.IntegerField(default=0)
    feed_given_kg = models.FloatField()
    date = models.DateField(auto_now_add=True)