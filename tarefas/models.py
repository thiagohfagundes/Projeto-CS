from django.db import models
from gestaocarteira.models import Cliente
#from negocios.models import Negocio
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Tarefa(models.Model):
    TIPO_TAREFA = [
        ("QBR", "QBR"),
        ("EBR", "EBR"),
        ("K", "Kickoff"),
        ("R", "Reunião"),
        ("L", "Ligação"),
        ("V", "Visita"),
        ("W", "Whatsapp"),
        ("O", "Outros")
    ]
    STATUS_TAREFA = [
        ("AG", "Agendada"),
        ("AT", "Atrasada"),
        ("FN", "Finalizada"),
        ("NR", "Não realizada"),
    ]
    OBJETIVO_TAREFA = [
        ("R", "Retenção"),
        ("N", "Negócio"),
        ("S", "Satisfação"),
        ("P", "Reunião periódica"),
        ("E", "Problema ou emergência")
    ]
    nome = models.CharField(max_length=124)
    objetivo = models.CharField(max_length=356)
    tipo_tarefa = models.CharField(max_length=3, choices=TIPO_TAREFA)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    #negocio = models.ForeignKey(Negocio, blank=True, null=True, on_delete=models.CASCADE)
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='criado_por')
    atribuido_a = models.ForeignKey(User, on_delete=models.CASCADE, related_name='atribuido_a')
    status_tarefa = models.CharField(max_length=3, choices=STATUS_TAREFA)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    data_da_tarefa = models.DateTimeField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('tarefas')