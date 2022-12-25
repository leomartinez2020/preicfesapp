from django.shortcuts import render

from .models import PreguntaEstandar, PreguntaUno, PreguntaLectura, OpcionLectura
from .models import SeccionEstandar, SeccionUno, SeccionLectura, Quiz, OpcionEstandar

def main(request):
    quiz_ciencias = Quiz.objects.filter(categoria='ciencias')
    quiz_mats = Quiz.objects.filter(categoria='matematicas')
    quiz_ingles = Quiz.objects.filter(categoria='ingles')
    quiz_sociales = Quiz.objects.filter(categoria='sociales')
    quiz_lectura = Quiz.objects.filter(categoria='lectura')
    context= {'ciencias': quiz_ciencias, 'matematicas': quiz_mats,
              'ingles': quiz_ingles, 'sociales': quiz_sociales, 'lectura': quiz_lectura}
    return render(request, 'icfesapp/main.html', context)

def prueba(request, slug, pk):
    quiz = Quiz.objects.get(pk=pk)
    secciones = quiz.get_secciones()
    context = {'secciones': secciones, 'quiz': quiz}
    return render(request, 'icfesapp/plantilla_preguntas.html', context)

def revisar(request, quiz_id):
    print(request.POST)
    quiz = Quiz.objects.get(pk=quiz_id)
    lista_preguntas = []
    lista_respuestas = []
    lista_correctas = []
    for item in request.POST:
        if item.startswith('pregunta'):
            respuesta, pregunta_id = helper2(request.POST[item])
            p = PreguntaUno.objects.get(pk=pregunta_id)
            correcta = p.palabra
            lista_preguntas.append(p)
            lista_respuestas.append(p.seccion.palabras[respuesta])
            lista_correctas.append(correcta)
        if item.startswith('lectura'):
            respuesta, pregunta_id = helper2(request.POST[item])
            p = PreguntaLectura.objects.get(pk=pregunta_id)
            correcta = p.opciones_lectura.get(es_correcta=True)
            lista_preguntas.append(p)
            lista_respuestas.append(respuesta)
            lista_correctas.append(correcta.texto)
        if item.startswith('estandar'):
            pregunta_id, respuesta_id = helper(request.POST[item])
            p = PreguntaEstandar.objects.get(pk=pregunta_id)
            correcta = p.opciones.get(es_correcta=True)
            lista_preguntas.append(p)
            lista_respuestas.append(OpcionEstandar.objects.get(pk=respuesta_id).texto)
            lista_correctas.append(correcta.texto)
        datos = zip(lista_preguntas, lista_respuestas, lista_correctas)
    context = {
        'quiz': quiz,
        'datos': datos
    }
    return render(request, 'icfesapp/resultados.html', context)

def helper(s):
    return [int(item) for item in s.split('-')]

def helper2(s):
    a, b = s.split('-')
    return [a, int(b)]
