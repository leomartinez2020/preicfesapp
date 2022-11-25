from django.db import models
from django.utils.text import slugify
from django.urls import reverse

from ckeditor.fields import RichTextField


class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre


class Post(models.Model):
    class Meta:
        ordering = ['-fecha_creacion']

    titulo = models.CharField(max_length=255, unique=True)
    info = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    contenido = RichTextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificado = models.DateTimeField(auto_now=True)
    fue_publicado = models.BooleanField(default=False)
    etiquetas = models.ManyToManyField(Etiqueta, blank=True)
    imagen = models.ImageField(upload_to='media', null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('blog:post', args=[str(self.slug)])
