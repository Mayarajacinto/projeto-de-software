from rest_framework import ModelViewSet
from ..serializers import StatusLivroSerializer
from ..models import StatusLivro

#a class herda os atributos de ModelViewSet
class StatusLivroViewSet(ModelViewSet):
    queryset = StatusLivro.objects.all()
    serializer_class = StatusLivroSerializer