from django.shortcuts import render, redirect

from solicitacao.forms import SolicitacaoForm


def solicitacao(request):
    if(request.user.is_authenticated):
        form = SolicitacaoForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            solicitatao = form.save()
            #return render(request, 'site/pedidos/agradecimentos.html', {'solicitacao': solicitatao})
        return render(request, 'solicitacao.html', {'form': form})
    return redirect('login/')
