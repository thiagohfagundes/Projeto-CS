from django.shortcuts import render

# Create your views here.
def tarefas(request):
    return render(request, "tarefas.html")