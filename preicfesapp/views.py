import logging

from random import shuffle

from django.shortcuts import render

from .models import Pregunta, Respuesta, PreguntaLectura, RespuestaLectura, Quiz

def error_404(request, exception):
    return render(request, 'preicfesapp/404.html')

def main(request):
    quiz_ciencias = Quiz.objects.filter(categoria='ciencias')
    quiz_mats = Quiz.objects.filter(categoria='matematicas')
    quiz_ingles = Quiz.objects.filter(categoria='ingles')
    quiz_sociales = Quiz.objects.filter(categoria='sociales')
    quiz_lectura = Quiz.objects.filter(categoria='lectura')
    context= {'ciencias': quiz_ciencias, 'matematicas': quiz_mats,
              'ingles': quiz_ingles, 'sociales': quiz_sociales, 'lectura': quiz_lectura}
    return render(request, 'preicfesapp/main.html', context)

def prueba(request, slug, pk):
    quiz = Quiz.objects.get(pk=pk)
    #preguntas = Pregunta.objects.filter(categoria=categoria)
    preguntas = quiz.pregunta_set.all()
    # Mezclar aleatoriamente las preguntas
    # preguntas = list(preguntas)
    # shuffle(preguntas)
    lecturas = quiz.lectura_set.all()
    if lecturas:
        context = {'lecturas': lecturas, 'preguntas': preguntas, 'quiz': quiz, 'numero': 3}
    else:
        context = {'preguntas': preguntas, 'quiz': quiz, 'numero': 0}
    return render(request, 'preicfesapp/plantilla_preguntas.html', context)

def prueba_lectura(request, slug, pk):
    quiz = Quiz.objects.get(pk=pk)
    lecturas = quiz.lectura_set.all()
    context = {'lecturas': lecturas, 'quiz': quiz}
    return render(request, 'preicfesapp/plantilla_lecturas.html', context)

def revisar(request, quiz_id):
    logging.info(request.POST)
    quiz = Quiz.objects.get(pk=quiz_id)
    lista_preguntas = []
    lista_respuestas = []
    lista_respuestas_correctas = []
    for item in request.POST:
        if item.startswith('lectura'):
            pregunta_id, respuesta_id = helper(request.POST[item])
            p = PreguntaLectura.objects.get(pk=pregunta_id)
            lista_preguntas.append(p)
            lista_respuestas.append(RespuestaLectura.objects.get(pk=respuesta_id))
            lista_correctas = p.respuestalectura_set.filter(es_correcta=True)[0]
            lista_respuestas_correctas.append(lista_correctas)
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
