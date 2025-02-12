from django.db import models
from .statusEvento import status

class cadastrarEventos(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateFieldfield()
    hora = models.TimeField()
    local = models.CharField(max_length=100)
    descricao = models.TextField()
    status = models.ForeignKey(status, on_delete=models.DO_NOTHING)
    
    class Meta:
        db_table = 'cadastrarEventos'
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'