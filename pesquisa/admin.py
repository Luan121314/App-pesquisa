from django.contrib import admin

# Register your models here.
from .models import Alternativa, Pergunta
admin.site.register(Pergunta)
admin.site.register(Alternativa)

# Passar para o admin do django as classe para add no bd
