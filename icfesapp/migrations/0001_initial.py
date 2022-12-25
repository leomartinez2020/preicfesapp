# Generated by Django 4.1.3 on 2022-12-19 16:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(help_text='titulo del quiz', max_length=100)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('categoria', models.CharField(choices=[('ciencias', 'Ciencias naturales'), ('matematicas', 'Matemáticas'), ('lectura', 'Lectura crítica'), ('ingles', 'Inglés'), ('sociales', 'Sociales y ciudadanas')], default='ciencias', max_length=12)),
                ('fecha_agregado', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'quizzes',
            },
        ),
        migrations.CreateModel(
            name='SeccionUno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='titulo', max_length=120, null=True)),
                ('texto', models.CharField(default='texto', max_length=120, null=True)),
                ('descripcion', models.TextField(blank=True, default='descripcion', null=True)),
                ('numeracion_inicio', models.IntegerField(blank=True, null=True)),
                ('numeracion_fin', models.IntegerField(blank=True, null=True)),
                ('tipo', models.CharField(choices=[('tipouno', 'Ingles Tipo 1'), ('tipolectura', 'Seccion Tipo lectura'), ('tipoestandar', 'Pregunta estándar')], default='estandar', max_length=16)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='icfesapp')),
                ('ejemplo', models.JSONField()),
                ('tema', models.CharField(max_length=120)),
                ('palabras', models.JSONField()),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secciones_uno', to='icfesapp.quiz')),
            ],
            options={
                'verbose_name_plural': 'secciones uno',
            },
        ),
        migrations.CreateModel(
            name='SeccionLectura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='titulo', max_length=120, null=True)),
                ('texto', models.CharField(default='texto', max_length=120, null=True)),
                ('descripcion', models.TextField(blank=True, default='descripcion', null=True)),
                ('numeracion_inicio', models.IntegerField(blank=True, null=True)),
                ('numeracion_fin', models.IntegerField(blank=True, null=True)),
                ('tipo', models.CharField(choices=[('tipouno', 'Ingles Tipo 1'), ('tipolectura', 'Seccion Tipo lectura'), ('tipoestandar', 'Pregunta estándar')], default='estandar', max_length=16)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='icfesapp')),
                ('ejemplo', models.JSONField(blank=True, null=True)),
                ('lectura', models.TextField(blank=True, null=True)),
                ('columnas', models.IntegerField(default=1)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secciones_lectura', to='icfesapp.quiz')),
            ],
            options={
                'verbose_name_plural': 'secciones lecturas',
            },
        ),
        migrations.CreateModel(
            name='SeccionEstandar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='titulo', max_length=120, null=True)),
                ('texto', models.CharField(default='texto', max_length=120, null=True)),
                ('descripcion', models.TextField(blank=True, default='descripcion', null=True)),
                ('numeracion_inicio', models.IntegerField(blank=True, null=True)),
                ('numeracion_fin', models.IntegerField(blank=True, null=True)),
                ('tipo', models.CharField(choices=[('tipouno', 'Ingles Tipo 1'), ('tipolectura', 'Seccion Tipo lectura'), ('tipoestandar', 'Pregunta estándar')], default='estandar', max_length=16)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='icfesapp')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secciones_estandar', to='icfesapp.quiz')),
            ],
            options={
                'verbose_name_plural': 'secciones estandar',
            },
        ),
        migrations.CreateModel(
            name='PreguntaUno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(blank=True, null=True)),
                ('explicacion', models.TextField(blank=True, null=True)),
                ('palabra', models.CharField(max_length=100)),
                ('seccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='preguntas', to='icfesapp.seccionuno')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PreguntaLectura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(blank=True, null=True)),
                ('explicacion', models.TextField(blank=True, null=True)),
                ('seccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='preguntas', to='icfesapp.seccionlectura')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PreguntaEstandar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(blank=True, null=True)),
                ('explicacion', models.TextField(blank=True, null=True)),
                ('preambulo', models.TextField(blank=True, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='media')),
                ('respuestas_tienen_imagen', models.BooleanField(default=False)),
                ('seccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='preguntas', to='icfesapp.seccionestandar')),
            ],
            options={
                'verbose_name_plural': 'preguntas estandar',
            },
        ),
        migrations.CreateModel(
            name='OpcionLectura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(blank=True, null=True)),
                ('es_correcta', models.BooleanField(default=False)),
                ('pregunta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='opciones_lectura', to='icfesapp.preguntalectura')),
            ],
            options={
                'verbose_name_plural': 'opciones lectura',
            },
        ),
        migrations.CreateModel(
            name='OpcionEstandar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(blank=True, null=True)),
                ('es_correcta', models.BooleanField(default=False)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='media')),
                ('pregunta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='opciones', to='icfesapp.preguntaestandar')),
            ],
            options={
                'verbose_name_plural': 'opciones estandar',
            },
        ),
    ]