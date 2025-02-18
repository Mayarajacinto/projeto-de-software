from rest_framework.viewsets import ModelViewSet
from ..serializers import CadastrarEventoSerializer
from ..models import CadastrarEventos

class CadastrarPessoasViewSet(ModelViewSet):
    queryset = CadastrarEventos.objects.all()
    serializer_class = CadastrarEventoSerializer