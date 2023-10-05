from django.urls import path
from . import views
from .views import RegistrarChurn, DetalhesChurn, EditarChurn


urlpatterns = [
    path('', views.churn, name='churn'),
    path('registrar_churn/', RegistrarChurn.as_view(), name='registrar_churn'),
    path('churn/editar_churn/<int:pk>', EditarChurn.as_view(), name='editar_churn'),
    path('cliente/<int:pk>', DetalhesChurn.as_view(), name='detalhes_churn'),
]