from django.db import models
from django.core.validators import MaxValueValidator

class aluno(models.Model):
    matricula = models.IntegerField(primary_key=True, validators=[MaxValueValidator(9999999999999999)])
    nome = models.CharField(max_length=100)
    datadenascimento = models.DateField(max_length=12, null= True)
    email = models.EmailField(max_length=30, null=True)
    def __str__(self) -> str:
            return self.nome