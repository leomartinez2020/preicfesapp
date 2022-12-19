from django.db import models

from django.utils.text import slugify

class Departamento(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Municipio(models.Model):
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    # TODO: use related_name
    #departamento = models.ForeignKey(Departamento, related_name='departamentos', on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class ColegioAbstract(models.Model):
    CALENDARIO = [('A', 'calendario A'), ('B', 'calendario B'), ('O', 'Otro')]
    NATURALEZA = [('OFICIAL', 'oficial'), ('NO OFICIAL', 'no oficial')]
    JORNADA = [
        ('MAÑANA', 'mañana'),
        ('TARDE', 'tarde'),
        ('NOCTURNA', 'nocturna'),
        ('FIN DE SEMANA', 'fin de semana'),
        ('ÚNICA', 'única'),
        ('COMPLETA', 'completa')
    ]
    nombre = models.CharField(max_length=100, blank=True, null=True)
    codinst = models.CharField(max_length=20, blank=True, null=True)
    ubicacion = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    calendario = models.CharField(max_length=2, choices=CALENDARIO, blank=True, null=True)
    naturaleza = models.CharField(max_length=12, choices=NATURALEZA, blank=True, null=True)
    evaluados = models.IntegerField(blank=True, null=True)
    matematicas = models.FloatField(blank=True, null=True)
    sociales = models.FloatField(blank=True, null=True)
    ingles = models.FloatField(blank=True, null=True)
    ciencias = models.FloatField(blank=True, null=True)
    lectura = models.FloatField(blank=True, null=True)
    jornada = models.CharField(max_length=20, choices=JORNADA, blank=True, null=True)
    periodo = models.CharField(max_length=6, blank=True, null=True)
    promponderado = models.FloatField(blank=True, null=True)
    puntajeglobal = models.FloatField(blank=True, null=True)
    slug = models.SlugField(max_length=200, null=True, blank=True)

    class Meta:
        abstract = True


class Colegio2020(ColegioAbstract):

    def __str__(self):
        return self.nombre

    # TODO agregar Meta ordering de acuerdo a promponderado
    def save(self, *args, **kwargs):
        try:
            suma = (self.matematicas + self.sociales + self.ciencias + self.lectura) * 3
            suma += self.ingles
            promponderado = suma / 13.0
            self.puntajeglobal = round(promponderado * 5, 2)
            self.promponderado = round(promponderado, 2)
        except TypeError:
            pass
        self.slug = slugify(self.nombre)
        #super(Colegio, self).save(*args, **kwargs)
        super().save(*args, **kwargs)


class Colegio(models.Model):
    CALENDARIO = [('A', 'calendario A'), ('B', 'calendario B'), ('O', 'Otro')]
    NATURALEZA = [('OFICIAL', 'oficial'), ('NO OFICIAL', 'no oficial')]
    JORNADA = [
        ('MAÑANA', 'mañana'),
        ('TARDE', 'tarde'),
        ('NOCTURNA', 'nocturna'),
        ('FIN DE SEMANA', 'fin de semana'),
        ('ÚNICA', 'única'),
        ('COMPLETA', 'completa')
    ]
    nombre = models.CharField(max_length=100, blank=True, null=True)
    codinst = models.CharField(max_length=20, blank=True, null=True)
    ubicacion = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    calendario = models.CharField(max_length=2, choices=CALENDARIO, blank=True, null=True)
    naturaleza = models.CharField(max_length=12, choices=NATURALEZA, blank=True, null=True)
    evaluados = models.IntegerField(blank=True, null=True)
    matematicas = models.FloatField(blank=True, null=True)
    sociales = models.FloatField(blank=True, null=True)
    ingles = models.FloatField(blank=True, null=True)
    ciencias = models.FloatField(blank=True, null=True)
    lectura = models.FloatField(blank=True, null=True)
    jornada = models.CharField(max_length=20, choices=JORNADA, blank=True, null=True)
    periodo = models.CharField(max_length=6, blank=True, null=True)
    promponderado = models.FloatField(blank=True, null=True)
    puntajeglobal = models.FloatField(blank=True, null=True)
    slug = models.SlugField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nombre

    # TODO agregar Meta ordering de acuerdo a promponderado
    def save(self, *args, **kwargs):
        try:
            suma = (self.matematicas + self.sociales + self.ciencias + self.lectura) * 3
            suma += self.ingles
            promponderado = suma / 13.0
            self.puntajeglobal = round(promponderado * 5, 2)
            self.promponderado = round(promponderado, 2)
        except TypeError:
            pass
        self.slug = slugify(self.nombre)
        #super(Colegio, self).save(*args, **kwargs)
        super().save(*args, **kwargs)

    def get_fields(self, model):
        return model._meta.get_fields()
