from rest_framework import serializers
from .models import Cliente, Vendedor, Produto


class ClienteSerializer(serializers.ModelSerializer):
    senha = serializers.CharField(write_only=True, required=False)
    email = serializers.CharField(write_only=True, required=False)
    sobrenome = serializers.CharField(write_only=True, required=False)
    cpf = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Cliente
        fields = ['nome', 'sobrenome', 'login', 'cpf',
                  'senha', 'guid',  'email']
        read_only_fields = ['guid']


def create(self, validated_data):
    senha = validated_data.pop('senha', None)
    email = validated_data.pop('email', None)
    sobrenome = validated_data.pop('sobrenome', None)
    cpf = validated_data.pop('cpf', None)
    Cliente = Cliente.objects.create(**validated_data)
    # Aqui você pode aplicar lógica com o código promocional, se houver
    return Cliente


class VendedorSerializer(serializers.ModelSerializer):
    senha = serializers.CharField(write_only=True, required=False)
    nomeComercial = serializers.CharField(write_only=True, required=False)
    email = serializers.CharField(write_only=True, required=False)
    sobrenome = serializers.CharField(write_only=True, required=False)
    cnpj = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Vendedor
        fields = ['nome', 'sobrenome', 'login', 'cnpj',
                  'senha', 'guid', 'nomeComercial', 'email']
        read_only_fields = ['guid']


def create(self, validated_data):
    senha = validated_data.pop('senha', None)
    email = validated_data.pop('email', None)
    nomeComercial = validated_data.pop('nomeComercial', None)
    sobrenome = validated_data.pop('sobrenome', None)
    cnpj = validated_data.pop('cnpj', None)
    Vendedor = Vendedor.objects.create(**validated_data)
    # Aqui você pode aplicar lógica com o código promocional, se houver
    return Vendedor


class ProdutoSerializer(serializers.ModelSerializer):
    quantidade = serializers.CharField(write_only=True, required=False)
    categoria = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'valor', 'quantidade',
                  'categoria', 'vendedor', 'guid']
        read_only_fields = ['guid']


def create(self, validated_data):
    quantidade = validated_data.pop('quantidade', None)
    categoria = validated_data.pop('categoria', None)
    Produto = Produto.objects.create(**validated_data)
    # Aqui você pode aplicar lógica com o código promocional, se houver
    return Produto


class UnicoClienteSerializer(serializers.ModelSerializer):
     class Meta:
        model = Cliente
        fields = ['nome', 'login',  'guid']
     
