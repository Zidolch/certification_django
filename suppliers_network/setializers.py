from rest_framework import serializers

from suppliers_network.models import NetworkObject, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name']
        read_only_fields = ("id", "name", "model", 'release_date')


class NetworkObjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkObject
        fields = '__all__'


class NetworkObjectSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, required=False)
    supplier = serializers.SlugRelatedField(slug_field='name', queryset=NetworkObject.objects.all())

    class Meta:
        model = NetworkObject
        fields = '__all__'
        read_only_fields = ('debt', 'created')
