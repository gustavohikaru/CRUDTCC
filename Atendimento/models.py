from django.db import models
from Aluno.models import aluno
from Psicologa.models import psicologa
from Indicacao.models import Indicacao

class Atendimento(models.Model):
    diaatendimento=models.DateField(max_length=12, primary_key=True)
    matriculaaluno=models.ForeignKey(aluno, on_delete=models.CASCADE, null=True, blank=True)
    SUAPPsicologa=models.ForeignKey(psicologa, on_delete=models.CASCADE, null=True, blank=True)
    indicacao=models.ForeignKey(Indicacao, on_delete=models.CASCADE, null=True, blank=True)
    observacoes = models.CharField(max_length=300)
class encontro(models.Model):
      diadoatendimento=models.ForeignKey(Atendimento, on_delete=models.CASCADE, null=True, blank=True)
      desenvolvimento = models.CharField(max_length=60, null=True)
      observacoes = models.CharField(max_length=300)

class motivo(models.Model):
    IDmotivo=models.AutoField(primary_key=True)

    motivogeral = models.ForeignKey(Atendimento, on_delete=models.CASCADE, null=True, blank=True)

    STATUS_CHOICES = (
        ('problema escolar', 'problema escolar'),
        ('sintoma psiquio', 'sintoma psiquio'),
    )
    caracteristicaspessoaisracionais=models.CharField(max_length=20,null=True)
    outros=models.CharField(max_length=40)
def get_status_display(self):
        return dict(self.STATUS_CHOICES).get(self.status)
class Meta:
        ordering = ('-motivogeral',)