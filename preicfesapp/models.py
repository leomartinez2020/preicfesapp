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

class PreguntaAbstract(models.Model):
    categoria = models.CharField(
        max_length=12,
        choices=PRUEBAS,
        default='ciencias',
        null=True,
        blank=True
    )
    contexto = models.TextField(null=True, blank=True)
    texto = models.TextField(null=True, blank=True)
    explicacion = models.TextField(null=True, blank=True)
    imagen = models.ImageField(upload_to='media', null=True, blank=True)
    respuestas_tienen_imagen = models.BooleanField(default=False)

    class Meta:
        abstract = True


class RespuestaAbstract(models.Model):
    texto = models.TextField(null=True, blank=True)
    imagen = models.ImageField(upload_to='media', null=True, blank=True)
    es_correcta = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Quiz(models.Model):
    '''A quiz template'''
    #setter = models.ForeignKey(User, related_name='setter')
    titulo = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    categoria = models.CharField(choices=PRUEBAS, default='ciencias', max_length=12)
    publicado = models.DateTimeField(blank=True, null=True)
    fecha_agregado = models.DateTimeField(default=timezone.now)
    fecha_modificado = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "quizzes"

    def save(self, *args, **kwargs):
        fecha_slug = self.fecha_modificado.strftime('%Y-%m-%d')
        self.slug = slugify(self.titulo + ' ' + fecha_slug)
        super(Quiz, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo

    #@property TODO
    def get_preguntas(self):
        return self.pregunta_set.all()

    def get_absolute_url(self):
        return reverse('preicfesapp:prueba', args=[str(self.pk)])


class Lectura(models.Model):
    titulo = models.CharField(max_length=120, null=True)
    contenido = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='media', null=True, blank=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '%s - %d' %(self.titulo, self.id)

    def get_preguntas(self):
        return self.preguntalectura_set.all()


class PreguntaLectura(PreguntaAbstract):
    lectura = models.ForeignKey(Lectura, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.texto

    def get_respuestas(self):
        return self.respuestalectura_set.all()


class RespuestaLectura(RespuestaAbstract):
    pregunta = models.ForeignKey(PreguntaLectura, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.texto

class Pregunta(models.Model):
    categoria = models.CharField(
        max_length=12,
        choices=PRUEBAS,
        default='ciencias',
        null=True,
        blank=True
    )
    contexto = models.TextField(null=True, blank=True)
    texto = models.TextField(null=True, blank=True)
    explicacion = models.TextField(null=True, blank=True)
    imagen = models.ImageField(upload_to='media', null=True, blank=True)
    respuestas_tienen_imagen = models.BooleanField(default=False)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.texto

    def get_respuestas(self):
        return self.respuesta_set.all()


class Respuesta(models.Model):
    texto = models.TextField(null=True, blank=True)
    imagen = models.ImageField(upload_to='media', null=True, blank=True)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, null=True, blank=True)
    es_correcta = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.imagen.name:
            self.texto = self.imagen.name
        super(Respuesta, self).save(*args, **kwargs)

    def __str__(self):
        return self.texto


class PreguntaInglesAbstract(models.Model):
    titulo = models.CharField(max_length=120)
    descripcion = models.TextField()
    lectura = models.TextField(null=True)

    class Meta:
        abstract = True


class PreguntaIngles1(PreguntaInglesAbstract):
    tema = models.CharField(max_length=120, null=True)


class Opcion1(models.Model):
    texto = models.CharField(max_length=150)
    palabra = models.CharField(max_length=80)
    pregunta = models.ForeignKey(PreguntaIngles1, related_name='opciones', on_delete=models.CASCADE)


class PreguntaIngles2(PreguntaInglesAbstract):
    imagen = models.ImageField(upload_to='media', null=True)


class Expresion2(models.Model):
    texto = models.TextField()
    pregunta = models.ForeignKey(PreguntaIngles2, related_name='expresiones', on_delete=models.CASCADE)
    es_ejemplo = models.BooleanField(default=False)


class Opcion2(models.Model):
    texto = models.CharField(max_length=150)
    expresion = models.ForeignKey(Expresion2, related_name='opciones', on_delete=models.CASCADE)
    es_correcta = models.BooleanField(default=False)

