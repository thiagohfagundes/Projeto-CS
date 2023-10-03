from django import forms
from .models import Tarefa

class CriaTarefa(forms.Form):
    class Meta:
        model = Tarefa
        fields = '__all__'
