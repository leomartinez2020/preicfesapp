# Generated by Django 4.1.3 on 2022-12-04 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('preicfesapp', '0005_remove_pregunta_quiz_pregunta_quiz'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lectura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField(blank=True, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='PreguntaLectura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(blank=True, choices=[('ciencias', 'Ciencias naturales'), ('matematicas', 'Matemáticas'), ('lectura', 'Lectura crítica'), ('ingles', 'Inglés'), ('sociales', 'Sociales y ciudadanas')], default='ciencias', max_length=12, null=True)),
                ('contexto', models.TextField(blank=True, null=True)),
                ('texto', models.TextField(blank=True, null=True)),
                ('explicacion', models.TextField(blank=True, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='media')),
                ('respuestas_tienen_imagen', models.BooleanField(default=False)),
                ('lectura', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='preicfesapp.lectura')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]