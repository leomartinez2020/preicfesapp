from django.contrib import admin

from .models import Pregunta, Respuesta, Quiz, PreguntaLectura, RespuestaLectura, Lectura

class RespuestaInline(admin.TabularInline):
    model = Respuesta
    extra = 1

class PreguntaAdmin(admin.ModelAdmin):
    inlines = [RespuestaInline]

class RespuestaLecturaInline(admin.TabularInline):
    model = RespuestaLectura
    extra = 1

class PreguntaLecturaAdmin(admin.ModelAdmin):
    inlines = [RespuestaLecturaInline]

admin.site.register(Quiz)
admin.site.register(Pregunta, PreguntaAdmin)
#admin.site.register(Pregunta)
admin.site.register(Respuesta)
admin.site.register(PreguntaLectura, PreguntaLecturaAdmin)
admin.site.register(RespuestaLectura)
admin.site.register(Lectura)
