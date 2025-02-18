from rest_framework.viewsets import ModelViewSet
from ..serializers import CadastraLivroSerializer
from ..models import CadastraLivro

class CadastrarLivroViewSet(ModelViewSet):
    queryset = CadastraLivro.objects.all()
    serializer_class = CadastraLivroSerializer
    
