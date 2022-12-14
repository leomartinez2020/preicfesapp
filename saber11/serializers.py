from rest_framework import serializers

from .models import Colegio, Departamento

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


class DepartamentoSerializer(serializers.ModelSerializer):
    municipio_set = serializers.StringRelatedField(many=True)

    class Meta:
        model = Departamento
        fields = ['nombre', 'municipio_set']
