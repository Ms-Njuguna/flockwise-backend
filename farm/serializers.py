from rest_framework import serializers
from .models import Flock, EggRecord, BirdSale, Expense

class FlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flock
        fields = '__all__'


class EggRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = EggRecord
        fields = '__all__'


class BirdSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BirdSale
        fields = '__all__'


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'