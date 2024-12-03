from django.db import models

# Create your models here.
class Alimento(models.Model):
    nome = models.CharField(max_length=20)
    proteina = models.FloatField()
    caloria = models.FloatField()
    carboidrato = models.FloatField()
    gordura = models.FloatField()
    sodio = models.FloatField()
    vitaminaC = models.FloatField()
    ferro = models.FloatField()
    magnesio = models.FloatField()
    calcio = models.FloatField()
    preco = models.FloatField()