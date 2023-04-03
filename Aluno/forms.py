from django import forms 

from models import aluno
class alunoform(forms.ModelForm):
    class meta:
        model = aluno
        fields = '__all__'