from django.db import models
from gestaocarteira.models import Cliente, Contrato
from django.contrib.auth.models import User

# Create your models here.
class Churn(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_churn = models.DateTimeField()
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
    responsavel = models.ForeignKey(User, on_delete=models.CASCADE)

