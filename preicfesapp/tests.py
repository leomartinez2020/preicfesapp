#from django.test import TestCase

from preicfesapp.models import Pregunta

#class PreguntaTestCase(TestCase):

def test_preguntas_tienen_una_respuesta_correcta():
    """ Cada pregunta debe tener una opción correcta """
    preguntas = Pregunta.objects.all()
    for pregunta in preguntas:
        queryset = pregunta.respuesta_set.filter(es_correcta=True)
        assert len(queryset) == 1
        respuesta = queryset[0]
        assert respuesta.es_correcta, 'hay respuesta correcta'

def test_preguntas_tienen_cuatro_respuestas():
    """ Cada pregunta debe tener 4 opciones correctas """
    preguntas = Pregunta.objects.all()
    for pregunta in preguntas:
        queryset = pregunta.respuesta_set.all()
        assert len(queryset) == 4, 'hay 4 opciones'

