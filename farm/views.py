from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Flock, EggRecord, BirdSale, Expense
from .serializers import (
    FlockSerializer,
    EggRecordSerializer,
    BirdSaleSerializer,
    ExpenseSerializer,
)

class FlockViewSet(ModelViewSet):
    queryset = Flock.objects.all()
    serializer_class = FlockSerializer


class EggRecordViewSet(ModelViewSet):
    queryset = EggRecord.objects.all()
    serializer_class = EggRecordSerializer


class BirdSaleViewSet(ModelViewSet):
    queryset = BirdSale.objects.all()
    serializer_class = BirdSaleSerializer


class ExpenseViewSet(ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

@api_view(['POST'])
def register(request):
    user = User.objects.create_user(
        username=request.data['username'],
        password=request.data['password']
    )
    return Response({"message": "User created"})