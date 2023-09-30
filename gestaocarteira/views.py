from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

# Create your views here.
def index(request):

    return render(request, "index.html")

class ListarClientes(ListView):
    model = Cliente
    template_name = 'clientes.html'

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