from rest_framework import ModelViewSet
from ..serializers import StatusEventoSerializer
from ..models import statusEvento

#a class herda os atributos de ModelViewSet
class StatusLivroViewSet(ModelViewSet):
    queryset = statusEvento.objects.all()
    serializer_class = StatusEventoSerializer