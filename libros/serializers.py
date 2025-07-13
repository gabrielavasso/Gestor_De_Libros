from rest_framework import serializers
from .models import Autor, Clasificacion, Libro

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class ClasificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clasificacion
        fields = '__all__'

class LibroSerializer(serializers.ModelSerializer):
    autor = AutorSerializer()
    clasificacion = ClasificacionSerializer()

    class Meta:
        model = Libro
        fields = '__all__'
