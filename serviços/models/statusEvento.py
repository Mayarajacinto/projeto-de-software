from django.db import models

class status(models.Model):
    status = models.CharField('Em planejamento' or 'Em andamento' or 'Finalizado' or 'Cancelado')
        
    def __str__(self):
        return status