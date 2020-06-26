from django.db import models
from django.core.validators import RegexValidator

from usuarios.models import User


class Solicitacao(models.Model):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Apenas números são permitidos')

    nome_completo = models.CharField(max_length=150)
    identidade = models.CharField(max_length=7, validators=[alphanumeric])
    cpf = models.CharField(max_length=11, validators=[alphanumeric])
    data_de_nascimento = models.DateField(blank=True, null=True)
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE)
    MODALIDADE_CHOICES = (
        ("D", "Débito"),
        ("C", "Crédito"),
    )

    modalidade_de_pagamento = models.CharField(max_length=1, choices=MODALIDADE_CHOICES, blank=False, null=False)
    numero_do_cartao = models.CharField(max_length=16, validators=[alphanumeric])
    nome_no_cartao =  models.CharField(max_length=30)
    validade = models.DateField()
    codigo_de_seguranca = models.CharField(max_length=3, validators=[alphanumeric])
    comprovante = models.FileField(blank=True, null=True)
    executada = models.BooleanField(default=False,null=False)

    def __str__(self):
        return self.nome_completo

    class Meta:
        verbose_name_plural = "Solicitações"
