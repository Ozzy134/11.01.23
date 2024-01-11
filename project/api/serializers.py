from rest_framework import serializers
from .models import Products

class ProductsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=25)
    price = serializers.IntegerField()
    description = serializers.CharField(max_length=120)
    date = serializers.DateField(read_only=True)
    is_available = serializers.BooleanField()

    def create(self, validated_data):
        return Products.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.date = validated_data.get('date', instance.date)
        instance.is_available = validated_data.get('is_available', instance.is_available)
        instance.save()
        return instance

