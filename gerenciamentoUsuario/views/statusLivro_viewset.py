from rest_framework import ModelViewSet
from ..serializers import StatusPessoaSerializer
from ..models import statusPessoa

#a class herda os atributos de ModelViewSet
class StatusLivroViewSet(ModelViewSet):
    queryset = statusPessoa.objects.all()
    serializer_class = StatusPessoaSerializer