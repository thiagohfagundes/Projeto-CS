from django.db import models
from gestaocarteira.models import Cliente, Usuario

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
    criado_por = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='criado_por')
    atribuido_a = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='atribuido_a')
    status_tarefa = models.CharField(max_length=3, choices=STATUS_TAREFA)