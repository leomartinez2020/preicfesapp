from django.contrib import admin

from .models import Pregunta, Respuesta, Quiz, PreguntaLectura, RespuestaLectura, Lectura

admin.site.register(Quiz)
admin.site.register(Pregunta)
admin.site.register(Respuesta)
admin.site.register(PreguntaLectura)
admin.site.register(RespuestaLectura)
admin.site.register(Lectura)
