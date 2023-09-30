# Generated by Django 4.2.5 on 2023-09-30 12:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tarefas', '0002_tarefa_data_atualizacao_tarefa_data_criacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='atribuido_a',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='atribuido_a', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='criado_por',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='criado_por', to=settings.AUTH_USER_MODEL),
        ),
    ]
