from django.db import models

class status(models.Model):
    status = models.CharField('Ativa', 'Inativa', 'Bloqueada')
        
    def __str__(self):
        return status