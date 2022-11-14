from random import shuffle

from django.shortcuts import render

from .models import Pregunta, Respuesta, Quiz

def index(request):
    return render(request, 'preicfesapp/main.html')

def prueba(request, categoria):
    quiz = Quiz.objects.get(categoria=categoria)
    preguntas = Pregunta.objects.filter(categoria=categoria)
    # Mezclar aleatoriamente las preguntas
    preguntas = list(preguntas)
    shuffle(preguntas)
    context = {'preguntas': preguntas, 'categoria': categoria, 'quiz': quiz}
    return render(request, 'preicfesapp/plantilla_preguntas.html', context)

def revisar(request, quiz_id):
    #print(request.POST)
    quiz = Quiz.objects.get(pk=quiz_id)
    lista_preguntas = []
    lista_respuestas = []
    lista_respuestas_correctas = []
    for item in request.POST:
        if item.startswith('pregunta'):
            pregunta_id, respuesta_id = helper(request.POST[item])
            p = Pregunta.objects.get(pk=pregunta_id)
            lista_preguntas.append(p)
            lista_respuestas.append(Respuesta.objects.get(pk=respuesta_id))
            lista_correctas = p.respuesta_set.filter(es_correcta=True)[0]
            lista_respuestas_correctas.append(lista_correctas)
    datos = zip(lista_preguntas, lista_respuestas, lista_respuestas_correctas)
    context = {
        'quiz': quiz,
        'datos': datos
    }
    return render(request, 'preicfesapp/resultados.html', context)

def helper(s):
    return [int(item) for item in s.split('-')]
