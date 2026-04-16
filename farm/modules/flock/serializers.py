from rest_framework import serializers
from .models import Flock

class FlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flock
        fields = "__all__"