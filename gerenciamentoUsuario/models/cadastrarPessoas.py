from django.db import models
from .statusPessoa import status

class cadastrarAdministrador(models.Model):
    #nome é uma string de tamanho max = 100
    nome = models.CharField(max_length=100)
    #cpf são 11 numeros
    cpf = models.SmallIntegerField(max_length=11) 
    #cargo 
    cargo = models.CharField(max_length=100)
    status = models.ForeignKey(status, on_delete=models.DO_NOTHING)
    #email é uma string de tamanho max = 100
    email = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'cadastrarAdministrador'
        verbose_name = 'Administrador'
        verbose_name_plural = 'Administradores'
        
class cadastarUsuario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.SmallIntegerField(max_length=11)
    status = models.ForeignKey(status, on_delete=models.DO_NOTHING)
    email = models.CharField(max_length=100)
    telefone = models.SmallIntegerField(max_length=11)
    
    class Meta:
        db_table = 'cadastrarUsuario'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'