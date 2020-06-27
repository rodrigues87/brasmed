from django.shortcuts import render, redirect

from solicitacao.forms import SolicitacaoForm


def solicitacao(request):
    if(request.user.is_authenticated):
        form = SolicitacaoForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            solicitacao = form.save(commit=False)
            solicitacao.vendedor = request.user
            solicitacao.save()

            return redirect('/')
        return render(request, 'solicitacao.html', {'form': form})
    return redirect('login/')
