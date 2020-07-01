from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Tarefa(models.Model):
    PRIORIDADE_CHOICES = [
        ("A", "Alta"),
        ("N", "Normal"),
        ("B", "Baixa")
    ]
    titulo = models.CharField(max_length=30, null=False, blank=False)
    descricao = models.CharField(max_length=30, null=False, blank=False)
    data_expiracao = models.DateField(null=False, blank=False)
    prioridade = models.CharField(max_length=1, choices=PRIORIDADE_CHOICES, null=False, blank=False)
    usuario = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

#class Cliente(models.Model):
#    nome = models.CharField(max_length=100)
#    data_nascimento = models.DateField(blank=True, null=True)
#    pontuacao = models.IntegerField(blank=True, null=True)
#    habilitacao = models.BooleanField(blank=True, null=True)
#    observacao = models.TextField(blank=True, null=True)

