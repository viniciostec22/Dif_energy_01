from django.db import models

# Create your models here.
class Unidade_consumidora(models.Model):

    #perimetro = models.CharField(max_length=60)
    estacao_bobeamento = models.CharField(max_length=60)
    demanda_contratada = models.FloatField()
    conta_contrato = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self)->str:
        return self.perimeter 
    
class Demanda_ativa_kw(models.Model):
    estacao = models.ForeignKey(Unidade_consumidora, on_delete=models.CASCADE)
    quantidade = models.FloatField()
    preco = models.FloatField()
    valor = models.FloatField()
   
    
class Demanda_complementar_kw(models.Model):
    estacao = models.ForeignKey(Unidade_consumidora, on_delete=models.CASCADE)
    quantidade = models.FloatField()
    preco = models.FloatField()
    valor = models.FloatField()
    