from django.db import models
from Aluno.models import aluno
from Psicologa.models import psicologa


class Atendimento(models.Model):
    diaatendimento=models.DateField(max_length=12, null= True)
    matriculaaluno=models.ForeignKey(aluno, on_delete=models.CASCADE)
    SUAPPsicologa=models.ForeignKey(psicologa, on_delete=models.CASCADE)
    observacoes = models.CharField(max_length=300)
    