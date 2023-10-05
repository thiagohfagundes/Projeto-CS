from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView
from .models import Churn

# Create your views here.
def churn(request):
    return render(request, "churn/churns.html", context={

    })

class RegistrarChurn(CreateView):
    model = Churn
    template_name = 'churn/registrarchurn.html'
    fields = '__all__'

class DetalhesChurn(DetailView):
    model = Churn
    template_name = 'churn/detalheschurn.html'

class EditarChurn(UpdateView):
    model = Churn
    template_name = 'churn/editarchurn.html'