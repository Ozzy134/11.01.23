from rest_framework import serializers
from .models import Cars, CarsModels, Parts, Film

class CarsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = '__all__'

class FilmSerializers(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'
