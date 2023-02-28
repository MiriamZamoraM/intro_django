from rest_framework import serializers
from .models import Libros


class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libros
        fields = '__all__'