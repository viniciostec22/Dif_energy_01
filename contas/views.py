from django.shortcuts import render
from .forms import FormUnidade_consumidora, FormDemanda_ativa

# Create your views here.
def cadastro(request):
    if request.method == "GET":
        form_demanda_ativa = FormDemanda_ativa
        form_unidade = FormUnidade_consumidora
        return render(request, 'contas/cadastro_fatura.html',{'forms':form_demanda_ativa, 'forms':form_unidade})