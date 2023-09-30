from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', ListarTarefas.as_view(), name='tarefas'),
    path('nova_tarefa/', AdicionarTarefa.as_view(), name='criar_tarefa'),
    path('editar_tarefa/', EditarTarefa.as_view(), name='editar_tarefa'),
    path('detalhes_tarefa/<int:pk>', DetalhesTarefa.as_view(), name='detalhes_tarefa')
]