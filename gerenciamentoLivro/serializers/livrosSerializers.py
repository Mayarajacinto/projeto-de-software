from rest_framework import serializers
from ..models import cadastrarLivro, statusLivro

# uma classe p cada modelo

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = statusLivro
        fields = [
            'status'
        ]

class LivroSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    
    class Meta:
        model = cadastrarLivro
        fields = [
            'id',
            'titulo',
            'autor',
            'editora',
            'status'
        ]
    def get_titulo(self, obj):
        return obj.livros.titulo
    
    def get_status(self, obj):
        return obj.status.status    

class RevistaSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    
    class Meta:
        model = cadastrarLivro
        fields = [
            'id',
            'titulo',
            'autor',
            'editora',
            'status'
        ]
        
    def get_titulo(self, obj):
        return obj.revistas.titulo
    
    def get_status(self, obj):
        return obj.status.status 
    
class ArtigoSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    
    class Meta:
        model = cadastrarLivro
        fields = [
            'id',
            'titulo',
            'autor',
            'status'
        ]
        
    def get_titulo(self, obj):
        return obj.artigos.titulo
    
    def get_status(self, obj):
        return obj.status.status         