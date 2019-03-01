from django.shortcuts import render

from .models import Pergunta
def index(request):
    todas = Pergunta.objects.all()
    return render(request, 'index.html',{"perguntas": todas
    })
def resposta(request, num_pergunta):
    pergunta = Pergunta.objects.get(pk=num_pergunta)
    return render(request, 'responder.html',{"pergunta": pergunta})

def votar(request):
    escolhida = Alternativa.objects.get(pk=voto)
    escolhida.votos +=1
    escolhida.save()
    voto =request.POST['escolha']
    return render(request, 'votar.html',{"numero": voto
    })

def resultados(request,num_pergunta):
    pergunta = Pergunta.objects.get(pk)
    return render(request, 'resultados.html')
