from rest_framework import serializers
from .models import EggRecord, BirdSale

class EggRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = EggRecord
        fields = "__all__"


class BirdSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BirdSale
        fields = "__all__"