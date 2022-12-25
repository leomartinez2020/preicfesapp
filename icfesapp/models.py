from itertools import chain
from django.utils import timezone

from django.db import models
from django.utils.text import slugify
from django.urls import reverse

PRUEBAS = [
    ('ciencias', 'Ciencias naturales'),
    ('matematicas', 'Matemáticas'),
    ('lectura', 'Lectura crítica'),
    ('ingles', 'Inglés'),
    ('sociales', 'Sociales y ciudadanas'),
]

TIPOS_DE_SECCIONES = [
    ('tipouno', 'Ingles Tipo 1'),
    ('tipolectura', 'Seccion Tipo lectura'),
    ('tipoestandar', 'Pregunta estándar'),
]

class Quiz(models.Model):
    titulo = models.CharField(max_length=100, help_text='titulo del quiz')
    slug = models.SlugField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    categoria = models.CharField(choices=PRUEBAS, default='ciencias', max_length=12)
    fecha_agregado = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "quizzes"

    def save(self, *args, **kwargs):
        fecha_slug = self.fecha_agregado.strftime('%Y-%m-%d')
        self.slug = slugify(self.titulo + ' ' + fecha_slug)
        super(Quiz, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo

    def get_secciones(self):
        return chain(self.secciones_uno.all(),
            self.secciones_lectura.all(),
            self.secciones_estandar.all())


class SeccionAbstract(models.Model):
    titulo = models.CharField(default='titulo', max_length=120, null=True)
    texto = models.CharField(default='texto', max_length=120, null=True)
    descripcion = models.TextField(default='descripcion', null=True, blank=True)
    numeracion_inicio = models.IntegerField(null=True, blank=True)
    numeracion_fin = models.IntegerField(null=True, blank=True)
    tipo = models.CharField(choices=TIPOS_DE_SECCIONES, default='estandar', max_length=16)
    imagen = models.ImageField(upload_to='icfesapp', null=True, blank=True)

    def __str__(self):
        return '%s - %d' %(self.titulo, self.id)

    class Meta:
        abstract = True

    def get_preguntas(self):
        return self.preguntas.all()


class PreguntaAbstract(models.Model):
    texto = models.TextField(null=True, blank=True)
    explicacion = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.texto


class OpcionAbstract(models.Model):
    texto = models.TextField(null=True, blank=True)
    es_correcta = models.BooleanField(default=False)

    class Meta:
        abstract = True


class SeccionUno(SeccionAbstract):
    quiz = models.ForeignKey(
        Quiz, related_name='secciones_uno',
        on_delete=models.CASCADE,
    )
    ejemplo = models.JSONField()
    tema = models.CharField(max_length=120)
    palabras = models.JSONField()

    class Meta:
        verbose_name_plural = "secciones uno"


class SeccionLectura(SeccionAbstract):
    quiz = models.ForeignKey(
        Quiz, related_name='secciones_lectura',
        on_delete=models.CASCADE,
    )
    ejemplo = models.JSONField(null=True, blank=True)
    lectura = models.TextField(null=True, blank=True)
    columnas = models.IntegerField(default=1)

    class Meta:
        verbose_name_plural = "secciones lecturas"


class SeccionEstandar(SeccionAbstract):
    quiz = models.ForeignKey(
        Quiz, related_name='secciones_estandar',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name_plural = "secciones estandar"


class PreguntaEstandar(PreguntaAbstract):
    seccion = models.ForeignKey(
        SeccionEstandar, related_name='preguntas',
        on_delete=models.CASCADE,
    )
    preambulo = models.TextField(null=True, blank=True)
    imagen = models.ImageField(upload_to='icfesapp', null=True, blank=True)
    respuestas_tienen_imagen = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "preguntas estandar"

    def get_opciones(self):
        return self.opciones.all()


class PreguntaUno(PreguntaAbstract):
    seccion = models.ForeignKey(
        SeccionUno, related_name='preguntas',
        on_delete=models.CASCADE,
    )
    palabra = models.CharField(max_length=100)


class PreguntaLectura(PreguntaAbstract):
    seccion = models.ForeignKey(
        SeccionLectura, related_name='preguntas',
        on_delete=models.CASCADE,
    )

    def get_opciones(self):
        return self.opciones_lectura.all()


class OpcionEstandar(OpcionAbstract):
    pregunta = models.ForeignKey(
        PreguntaEstandar, related_name='opciones',
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    imagen = models.ImageField(upload_to='icfesapp', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.imagen.name:
            self.texto = self.imagen.name
        super().save(*args, **kwargs)

    def __str__(self):
        return self.texto

    class Meta:
        verbose_name_plural = "opciones estandar"


class OpcionLectura(OpcionAbstract):
    pregunta = models.ForeignKey(
        PreguntaLectura, related_name='opciones_lectura',
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    class Meta:
        verbose_name_plural = "opciones lectura"

    def __str__(self):
        return self.texto
