from django.db import models
from django.core.validators import MaxValueValidator
class psicologa(models.Model):
    SUAP = models.IntegerField(primary_key=True, validators=[MaxValueValidator(9999999)])
    nome = models.CharField(max_length=100)
    def __str__(self) -> str:
            return self.nome