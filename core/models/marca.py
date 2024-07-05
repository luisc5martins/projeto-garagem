from django.db import models


class Marca(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome} ({self.id}) ({self.nacionalidade})"
    
    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"