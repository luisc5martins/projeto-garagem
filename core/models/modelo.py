from django.db import models


class Modelo(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome.upper()} ({self.id})"
    
    class Meta:
        verbose_name = "Modelo"
        verbose_name_plural = "Modelos"