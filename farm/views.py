from django.contrib.auth import get_user_model, authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Flock, EggRecord, BirdSale, Expense
from .serializers import (
    FlockSerializer,
    EggRecordSerializer,
    BirdSaleSerializer,
    ExpenseSerializer,
)

User = get_user_model()
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
        email=request.data['email'],
        password=request.data['password'],
    )
    return Response({"message": "User created"})


@api_view(['POST'])
def login(request):
    user = authenticate(
        username=request.data['username'],
        password=request.data['password']
    )

    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        })

    return Response({"error": "Invalid credentials"}, status=400)

@api_view(['POST'])
def ai_assistant(request):
    question = request.data.get("question")

    # SIMPLE VERSION (we upgrade later)
    if "eggs" in question.lower():
        answer = "Ensure 14 hours of light and proper feeding for better egg production."
    else:
        answer = "Focus on feed quality, hygiene, and bird health."

    return Response({"answer": answer})