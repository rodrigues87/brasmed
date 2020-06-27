from django import forms
from .models import Solicitacao


class SolicitacaoForm(forms.ModelForm):
    class Meta:
        model = Solicitacao
        fields = ['nome_completo', 'identidade', 'cpf', 'data_de_nascimento', 'vendedor', 'modalidade_de_pagamento',
                  'numero_do_cartao','nome_no_cartao','validade','codigo_de_seguranca','proposta_frente','proposta_verso',
                  'foto_identidade','foto_cpf']
        # produtos = forms.ModelChoiceField(queryset=Produto.objects.all(), widget=forms.Select(attrs={'onchange': "myFunction();"}))
