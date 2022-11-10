from django.contrib import admin

from .models import Pregunta, RespuestaMultiple, Quiz

admin.site.register(Quiz)
admin.site.register(Pregunta)
admin.site.register(RespuestaMultiple)
