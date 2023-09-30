from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("gestaocarteira.urls")),
    path('produtos/', include("produtos.urls")),
    path('tarefas/', include("tarefas.urls")),
    path('contas/', include("usuarios.urls")),
    path('contas/', include('django.contrib.auth.urls'))
]
