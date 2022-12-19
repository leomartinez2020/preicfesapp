# Generated by Django 4.1.3 on 2022-12-04 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('preicfesapp', '0008_lectura_quiz'),
    ]

    operations = [
        migrations.CreateModel(
            name='RespuestaLectura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(blank=True, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='media')),
                ('es_correcta', models.BooleanField(default=False)),
                ('pregunta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='preicfesapp.preguntalectura')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
