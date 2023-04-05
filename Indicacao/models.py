from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator

class responsavel(models.Model):
    id_resp=models.AutoField(primary_key=True)
    nomeresponsavel=models.CharField(max_length=20, null=True)
    telefone = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', # expressão regular que valida números de telefone
        message="O número de telefone deve estar no formato: '+999999999'. Até 15 dígitos permitidos."
    )
    endereco=models.CharField(max_length=30)
    email_responsavel=models.CharField(max_length=30,null=True)
    
class Indicacao(models.Model):
    Indicacao=models.AutoField(primary_key=True)
    idresp=models.ForeignKey(responsavel, on_delete=models.CASCADE, null=True, blank=True)
    SUAPServidor=models.IntegerField(validators=[MaxValueValidator(9999999)], null=True )
