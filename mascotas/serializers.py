from rest_framework import serializers
from mascotas.models import Mascota,Responsable

class ResponsableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsable
        fields = '__all__'

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = '__all__'


# rellenar después con class ProductoSerializer... CategoriaSerializer, etc