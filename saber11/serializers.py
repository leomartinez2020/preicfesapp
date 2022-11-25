from rest_framework import serializers

from .models import Colegio

class ColegioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colegio
        fields = ['nombre', 'ubicacion', 'evaluados',
            'calendario', 'naturaleza', 'jornada',
            'ingles', 'matematicas',
            'ciencias', 'sociales',
            'lectura', 'promponderado',
            'puntajeglobal', 'periodo',
        ]
