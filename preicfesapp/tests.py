from django.test import TestCase

from .models import Pregunta

class PreguntaTestCase(TestCase):
    def setUp(self):
        pass

    def test_preguntas_tienen_una_respuesta_correcta(self):
        """ Cada pregunta debe tener una opción correcta """
        preguntas = Pregunta.objects.all()
        for pregunta in preguntas:
            queryset = pregunta.respuesta_set.filter(es_correcta=True)
            self.assertEqual(len(queryset), 1)
            respuesta = queryset[0]
            self.assertTrue(respuesta.es_correcta)
