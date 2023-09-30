from django.urls import path
from . import views
from .views import ListarClientes, AdicionarCliente, DetalhesCliente, EditarCliente
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/', ListarClientes.as_view(), name='clientes'),
    path('adicionar_cliente/', AdicionarCliente.as_view(), name='adicionar_cliente'),
    path('cliente/editar_cliente/<int:pk>', EditarCliente.as_view(), name='editar_cliente'),
    path('cliente/<int:pk>', DetalhesCliente.as_view(), name='detalhes_cliente'),
    path('<int:pk>/password/', auth_views.PasswordChangeView.as_view(template_name='registration/mudarsenha.html'), name='editarsenha')
]