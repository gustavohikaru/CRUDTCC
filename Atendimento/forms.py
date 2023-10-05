from django import forms
from .models import Atendimento


class AtendimentoForm(forms.ModelForm):
    class Meta:
        model = Atendimento
        fields = '__all__'

    diaatendimento = forms.DateField(label='Dia do atendimento')
    observacoes = forms.CharField(widget=forms.Textarea)