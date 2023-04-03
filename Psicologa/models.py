from django.db import models

class psicologa(models.Model):
    SUAP = models.CharField(max_length=7, null = True)
    nome = models.CharField(max_length=100)
    def __str__(self) -> str:
            return self.nome