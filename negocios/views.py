from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Negocio

# Create your views here.
class ListarNegocios(ListView):
    model = Negocio
    paginate_by = 25
    template_name = 'negocios/negocios.html'

class AdicionarNegocio(CreateView):
    model = Negocio
    template_name = 'clientes/criarnegocio.html'
    fields = '__all__'

class EditarNegocio(UpdateView):
    model = Negocio
    template_name = 'negocios/editarnegocio.html'
    fields = '__all__'

class DetalhesNegocio(DetailView):
    model = Negocio
    template_name = 'negocios/detalhesnegocio.html'