from django.urls import path
from .views import ListarNegocios, AdicionarNegocio, EditarNegocio, DetalhesNegocio
from . import views

urlpatterns = [
    path('negocios/', ListarNegocios.as_view(), name='negocios'),
    path('adicionar_negocio/', AdicionarNegocio.as_view(), name='adicionar_negocio'),
    path('negocio/editar_negocio/<int:pk>', EditarNegocio.as_view(), name='editar_negocio'),
    path('negocio/<int:pk>', DetalhesNegocio.as_view(), name='detalhes_negocio'),
]