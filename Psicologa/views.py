from django.urls import reverse_lazy
from .models import psicologa
from django.views.generic import ListView,CreateView,UpdateView,DetailView,DeleteView

class PsicologaList(ListView):
    model= psicologa   
    queryset = psicologa.objects.all()


class PsicologaCreate(CreateView):
    model= psicologa 
    fields='__all__'
    success_url = reverse_lazy('Psicologa:list')

class PsicologaUpdate(UpdateView):
    model= psicologa
    fields='__all__'
    success_url = reverse_lazy('Psicologa:list')

class Psicologadetail(DetailView):
    queryset = psicologa.objects.all()

class PsicologaDelete(DeleteView):
    queryset = psicologa.objects.all()
    success_url = reverse_lazy('Aluno:list')