from django.contrib import admin

from .models import Pregunta, Respuesta, Quiz

admin.site.register(Quiz)
admin.site.register(Pregunta)
admin.site.register(Respuesta)
