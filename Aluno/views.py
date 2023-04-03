from django.urls import reverse_lazy
from .models import aluno
from django.views.generic import ListView,CreateView,UpdateView,DetailView,DeleteView

class AlunoList(ListView):
    model= aluno   
    queryset = aluno.objects.all()


class AlunoCreate(CreateView):
    model= aluno
    fields='__all__'
    success_url = reverse_lazy('Aluno:list')

class AlunoUpdate(UpdateView):
    model= aluno
    fields='__all__'
    success_url = reverse_lazy('Aluno:list')

class Alunodetail(DetailView):
    queryset = aluno.objects.all()

class AlunoDelete(DeleteView):
    queryset = aluno.objects.all()
    success_url = reverse_lazy('Aluno:list')