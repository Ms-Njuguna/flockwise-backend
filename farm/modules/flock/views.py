from rest_framework.viewsets import ModelViewSet
from .models import Flock
from .serializers import FlockSerializer

class FlockViewSet(ModelViewSet):
    queryset = Flock.objects.all()
    serializer_class = FlockSerializer