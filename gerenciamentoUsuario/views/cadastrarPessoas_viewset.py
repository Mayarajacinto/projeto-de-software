from rest_framework.viewsets import ModelViewSet
from ..serializers import CadastrarPessoasSerializer
from ..models import CadastrarPessoas

class CadastrarPessoasViewSet(ModelViewSet):
    queryset = CadastrarPessoas.objects.all()
    serializer_class = CadastrarPessoasSerializer