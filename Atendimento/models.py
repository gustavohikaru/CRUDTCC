from django.db import models
from Aluno.models import Aluno
from Aluno.models import Psicologa


class Atendimento(models.Model):
    diaatendimento=models.DateField(max_length=12, null= True)
    matriculaaluno=models.ForeignKey(Aluno, on_delete=models.CASCADE)
    SUAPPsicologa=models.ForeignKey(Psicologa, on_delete=models.CASCADE)
    observacoes = models.CharField(max_length=300)
    