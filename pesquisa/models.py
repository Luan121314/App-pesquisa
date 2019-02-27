from django.db import models
from django.utils import timezone

class Pergunta(models.Model):
    texto = models.CharField(max_length=300)
    data = models.DateTimeField(default = timezone.now)

class Alternativa(models.Model):
    pergunta = models.foreignKey(Pergunta, on_delete = models.CASCADE)
    texto = models.CharField(max_length=150)
    votos = models.IntegerField(default=0)