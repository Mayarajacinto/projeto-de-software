from rest_framework import serializers
from .. models import cadastarEvento, statusEvento

class StatusEvento(serializers.ModelSerializer):
    class Meta:
        model = statusEvento
        fields = [
            'status',
        ]

class CadastrarEventoSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    
    class Meta:
        model = cadastarEvento
        fields = [
            'id',
            'nome',
            'data',
            'horario',
            'local',
            'descricao',
            'status',
        ]
        
    def get_status(self, obj):
        return obj.status.status

    def get_nome(self, obj):
        return obj.cadastrarEvento.nome

    def get_data(self, obj):
        return obj.cadastrarEvento.data

    def get_horario(self, obj):
        return obj.cadastrarEvento.horario

    def get_local(self, obj):
        return obj.cadastrarEvento.local

    def get_descricao(self, obj):
        return obj.cadastrarEvento.descricao

    def get_status(self, obj):
        return obj.status.status