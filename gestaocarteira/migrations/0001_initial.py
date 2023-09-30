# Generated by Django 4.2.5 on 2023-09-23 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carteira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('descricao', models.CharField(blank=True, max_length=300, null=True)),
                ('responsavel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuarios.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('cidade', models.CharField(max_length=250)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('cpf_cnpj', models.CharField(max_length=20)),
                ('identificador', models.CharField(blank=True, max_length=150, null=True)),
                ('porte', models.CharField(blank=True, max_length=30, null=True)),
                ('ciclo_de_vida', models.CharField(choices=[('O', 'Onboarding'), ('R', 'Risco'), ('E', 'Expansão'), ('P', 'Promoção')], max_length=1)),
                ('nota_NPS', models.FloatField(max_length=4)),
                ('carteira', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestaocarteira.carteira')),
            ],
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_início', models.DateField()),
                ('status_contrato', models.CharField(choices=[('A', 'Ativo'), ('C', 'Cancelado'), ('E', 'Expirado'), ('S', 'Suspenso')], max_length=1)),
                ('MRR', models.FloatField(blank=True, max_length=12, null=True)),
                ('NRR', models.FloatField(blank=True, max_length=12, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestaocarteira.cliente')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.produto')),
            ],
        ),
    ]