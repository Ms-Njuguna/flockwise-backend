from rest_framework.viewsets import ModelViewSet
from .models import EggRecord, BirdSale
from .serializers import EggRecordSerializer, BirdSaleSerializer

class EggRecordViewSet(ModelViewSet):
    queryset = EggRecord.objects.all()
    serializer_class = EggRecordSerializer


class BirdSaleViewSet(ModelViewSet):
    queryset = BirdSale.objects.all()
    serializer_class = BirdSaleSerializer