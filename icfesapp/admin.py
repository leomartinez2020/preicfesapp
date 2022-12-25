from django.contrib import admin

from .models import (
    PreguntaEstandar, PreguntaUno, PreguntaLectura,
    SeccionEstandar, SeccionUno, SeccionLectura,
    Quiz, OpcionLectura, OpcionEstandar
)

admin.site.register(Quiz)
admin.site.register(PreguntaEstandar)
admin.site.register(PreguntaUno)
admin.site.register(PreguntaLectura)
admin.site.register(SeccionEstandar)
admin.site.register(SeccionUno)
admin.site.register(SeccionLectura)
admin.site.register(OpcionLectura)
admin.site.register(OpcionEstandar)
