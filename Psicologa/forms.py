from django import forms 

from models import psicologa
class alunoform(forms.ModelForm):
    class meta:
        model = psicologa
        fields = '__all__'