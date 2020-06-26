from django.contrib import admin

# Register your models here.
from solicitacao.models import Solicitacao


class SolicitacaoAdmin(admin.ModelAdmin):
    list_display = ['nome_completo', 'identidade', 'cpf', 'data_de_nascimento','vendedor','modalidade_de_pagamento']
    list_display_links = ['nome_completo']


admin.site.register(Solicitacao, SolicitacaoAdmin)