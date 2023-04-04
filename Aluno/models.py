from django.db import models

class aluno(models.Model):
    matricula = models.CharField(primary_key=True, max_length=16)
    nome = models.CharField(max_length=100)
    datadenascimento = models.DateField(max_length=12, null= True)
    email = models.EmailField(max_length=30, null=True)
    def __str__(self) -> str:
            return self.nome