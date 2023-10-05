from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from produtos.models import Produto
from gestaocarteira.models import Cliente

# Create your models here.
class Negocio(models.Model):
    STATUS_NEGOCIO = [
        ("O", "Oportunidade"),
        ("C", "Contato feito"),
        ("N", "Em negociação"),
        ("F", "Fechado")
    ]
    nome = models.CharField(max_length=155)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, null=True, blank=True)
    proprietario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    status_do_negocio = models.CharField(max_length=1, choices=STATUS_NEGOCIO, default='O')
    valor_estimado = models.FloatField(max_length=10, blank=True, null=True)
    data_fechamento = models.DateTimeField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('negocios')