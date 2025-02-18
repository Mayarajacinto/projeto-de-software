from rest_framework import serializers
from ..models import cadastrarPessoas, statusPessoa

class StatusPessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = statusPessoa
        fields = [
            'status',
        ]
        
class CadastrarAdministradorSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    
    class Meta:
        model = cadastrarPessoas
        fields = [
            'id',
            'nome',
            'cpf',
            'cargo',
            'status',
            'email',
        ]
        
    def get_status(self, obj):
        return obj.status.status
    
    def get_nome(self, obj):
        return obj.cadastrarAdministrador.nome 
    
class CadastrarUsuarioSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    
    class Meta:
        model = cadastrarPessoas
        fields = [
            'id',
            'nome',
            'cpf',
            'status',
            'email',
            'telefone',
        ]
        
    def get_status(self, obj):
        return obj.status.status
    
    def get_nome(self, obj):
        return obj.cadastrarUsuario.nome
    
    def get_cpf(self, obj):
        return obj.cadastrarUsuario.cpf
    
    def get_telefone(self, obj):
        return obj.cadastrarUsuario.telefone
    
    