from django.db import models

# Create your models here.
class Usuario(models.Model):
    FUNCOES = [
        ("CSM", "CSM"),
        ("ADM", "Administração")
    ]
    nome = models.CharField(max_length=128)
    funcao = models.CharField(max_length=3, choices=FUNCOES)
    data_admissao = models.DateField(null=True, blank=True)
    data_login = models.DateField()