from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from produtos.models import Produto

class Carteira(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=300, blank=True, null=True)
    responsavel = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

# Create your models here.
class Cliente(models.Model):
    CICLO_VIDA = [
        ("O", "Onboarding"),
        ("R", "Risco"),
        ("E", "Expansão"),
        ("P", "Promoção")
    ]
    nome = models.CharField(max_length=150)
    cidade = models.CharField(max_length=250)
    data_nascimento = models.DateField(null=True, blank=True)
    cpf_cnpj = models.CharField(max_length=20)
    identificador = models.CharField(max_length=150, blank=True, null=True)
    porte = models.CharField(max_length=30, blank=True, null=True)
    carteira = models.ForeignKey(Carteira, on_delete=models.SET_NULL, blank=True, null=True)
    ciclo_de_vida = models.CharField(max_length=1, choices=CICLO_VIDA)
    nota_NPS = models.FloatField(max_length=4)
    # incluir tarefas com relação onetomany

    def get_absolute_url(self):
        return reverse('clientes')

class Contrato(models.Model):
    STATUS_CONTRATO = [
        ("A", "Ativo"),
        ("C", "Cancelado"),
        ("E", "Expirado"),
        ("S", "Suspenso")
    ]
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_início = models.DateField()
    data_final = models.DateField(null=True, blank=True)
    status_contrato = models.CharField(max_length=1, choices=STATUS_CONTRATO)
    MRR = models.FloatField(max_length=12, blank=True, null=True)
    NRR = models.FloatField(max_length=12, blank=True, null=True)

