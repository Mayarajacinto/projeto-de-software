from django.db import models
from .statusLivro import status
    
class cadastrarLivro(models.Model):
    título = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    #importando a classe status, id estrangeiro da tabela status
    # cascade = se o status for deletado, o livro será deletado
    # do_noting = se o status for deletado, o livro não será deletado
    status = models.ForeignKey(status, on_delete=models.DO_NOTHING)
    
    class Meta:
        db_table = 'cadastrarLivros'
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
        
class cadastrarRevista(models.Model):
    título = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'cadastrarRevista'
        verbose_name = 'Revista'
        verbose_name_plural = 'Revistas'
        
class cadastrarArtigo(models.Model):
    título = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'cadastrarArtigo'
        verbose_name = 'Artigo'
        verbose_name_plural = 'Artigos'
        


