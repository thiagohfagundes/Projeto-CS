from django.db import models

class Produto(models.Model):
    TIPO_COBRANCA = [
        ("NRR", "Não recorrente"),
        ("MRR", "Recorrente")
    ]
    nome = models.CharField(max_length=124)
    valor = models.FloatField(max_length=14)
    tipo_cobranca = models.CharField(max_length=3, choices=TIPO_COBRANCA)
    plano = models.CharField(max_length=124)
