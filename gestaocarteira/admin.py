from django.contrib import admin
from .models import Carteira, Cliente, Contrato

# Register your models here.
admin.site.register(Carteira)
admin.site.register(Cliente)
admin.site.register(Contrato)
