from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Negocio(models.Model):
    nome = models.CharField(max_length=155)
    proprietario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    data_da_tarefa = models.DateTimeField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('negocios')