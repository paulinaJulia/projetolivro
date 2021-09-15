from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    editora= models.CharField(max_length=200)
    autor = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'

    def __str__(self):
        return self.titulo