from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

# Create your views here.
def index(request):

    return render(request, "index.html")

class ListarClientes(ListView):
    model = Cliente
    template_name = 'clientes/clientes.html'

class AdicionarCliente(CreateView):
    model = Cliente
    template_name = 'clientes/criarcliente.html'
    fields = '__all__'

class EditarCliente(UpdateView):
    model = Cliente
    template_name = 'clientes/editarcliente.html'
    fields = '__all__'

class DetalhesCliente(DetailView):
    model = Cliente
    template_name = 'clientes/detalhescliente.html'

class DeletarCliente(DeleteView):
    model = Cliente
    template_name = 'clientes/deletarcliente.html'
    success_url = reverse_lazy('clientes')