from rest_framework import serializers
from .models import Cliente, Vendedor, Produto


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        exclude = []
        read_only_fields = ['guid', 'id']


class VendedorSerializer(serializers.ModelSerializer):
    senha = serializers.CharField(write_only=True, required=False)
    nomeComercial = serializers.CharField(write_only=True, required=False)
    email = serializers.CharField(write_only=True, required=False)
    sobrenome = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Vendedor
        fields = ['nome', 'sobrenome', 'login',
                  'senha', 'guid', 'nomeComercial', 'email']
        read_only_fields = ['guid']


def create(self, validated_data):
    senha = validated_data.pop('senha', None)
    email = validated_data.pop('email', None)
    nomeComercial = validated_data.pop('nomeComercial', None)
    sobrenome = validated_data.pop('sobrenome', None)
    Vendedor = Vendedor.objects.create(**validated_data)
    # Aqui você pode aplicar lógica com o código promocional, se houver
    return Vendedor


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        exclude = []
        read_only_fields = ['guid', 'id']
