from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):
    FUNCOES = [
        ("CSM", "CSM"),
        ("ADM", "Administração")
    ]
    usuario = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    funcao = models.CharField(max_length=3, choices=FUNCOES)
    data_admissao = models.DateField(null=True, blank=True)
    foto_perfil = models.ImageField(upload_to='imagens/', null=True, blank=True)
    descricao = models.TextField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return str(self.usuario)
