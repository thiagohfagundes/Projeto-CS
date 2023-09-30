from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

# Create your views here
class ListarTarefas(ListView):
    model = Tarefa
    template_name = 'tarefas/tarefas.html'

class AdicionarTarefa(CreateView):
    model = Tarefa
    template_name = 'tarefas/criar_tarefas.html'
    fields = '__all__'

class EditarTarefa(UpdateView):
    model = Tarefa
    template_name = 'tarefas/editar_tarefa.html'

class DetalhesTarefa(DetailView):
    model = Tarefa
    template_name = 'tarefas/detalhes_tarefa.html'