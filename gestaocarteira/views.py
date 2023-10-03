from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

# Create your views here.
def index(request):

    return render(request, "index.html")

class ListarClientes(ListView):
    model = Cliente
    paginate_by = 25
    template_name = 'clientes/negocios.html'

class AdicionarCliente(CreateView):
    model = Cliente
    template_name = 'clientes/criarnegocio.html'
    fields = '__all__'

class EditarCliente(UpdateView):
    model = Cliente
    template_name = 'clientes/editarnegocio.html'
    fields = '__all__'

class DetalhesCliente(DetailView):
    model = Cliente
    template_name = 'clientes/detalhesnegocio.html'

class DeletarCliente(DeleteView):
    model = Cliente
    template_name = 'clientes/deletarnegocio.html'
    success_url = reverse_lazy('clientes')