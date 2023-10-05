from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Atendimento
from django.views.generic import ListView,CreateView,UpdateView,DetailView,DeleteView

class AtendimentoList(ListView):
    model= Atendimento   
    queryset = Atendimento.objects.all()


class AtendimentoCreate(CreateView):
    model= Atendimento
    fields='__all__'
    success_url = reverse_lazy('Atendimento:list')

class AtendimentoUpdate(UpdateView):
    model= Atendimento
    fields='__all__'
    success_url = reverse_lazy('Atendimento:list')

class Atendimentodetail(DetailView):
    queryset = Atendimento.objects.all()

class AtendimentoDelete(DeleteView):
    queryset = Atendimento.objects.all()
    success_url = reverse_lazy('Atendimento:list')