from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from .models import Unidade_consumidora, Demanda_ativa_kw, Demanda_complementar_kw

class FormUnidade_consumidora(ModelForm):
    class Meta: 
        model = Unidade_consumidora
        fields = '__all__'
        
class FormDemanda_ativa(ModelForm):
    class Meta:
        model = Demanda_ativa_kw
        fields = '__all__'
        
        
class FormDemanda_complementar(ModelForm):
    class Meta:
        model = Demanda_complementar_kw
        fields = '__all__'