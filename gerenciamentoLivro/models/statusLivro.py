from django.db import models

class status(models.Model):
    status = models.CharField('Disponível', 'Emprestado', 'Reservado', 'Emprestado e Reservado')
        
    def __str__(self):
        return status