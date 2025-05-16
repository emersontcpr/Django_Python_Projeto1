from rest_framework import viewsets, generics
from rest_framework.generics import RetrieveAPIView
from rest_framework.exceptions import NotFound
from .models import Cliente, Vendedor, Produto
from Loja.serializers import ClienteSerializer, VendedorSerializer, ProdutoSerializer, UnicoClienteSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class VendedorViewSet(viewsets.ModelViewSet):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class UnicoClienteViewSet(RetrieveAPIView):
    serializer_class = ClienteSerializer

    def get_object(self):
        queryset = Cliente.objects.filter(guid=self.kwargs['guid']).first()
        return queryset


class UnicoVendedorViewSet(RetrieveAPIView):
    def get_object(self):
        queryset = Vendedor.objects.filter(guid=self.kwargs['guid']).first()
        return queryset
    serializer_class = VendedorSerializer


class ListarProdutoPorVendedorViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Produto.objects.filter(vendedor_id=self.kwargs['id'])
        return queryset
    serializer_class = ProdutoSerializer


class UnicoProdutoViewSet(RetrieveAPIView):
    serializer_class = ProdutoSerializer

    def get_object(self):
        guid = self.kwargs['guid']
        produto = Produto.objects.filter(guid=guid).first()
        if not produto:
            raise NotFound("Produto não encontrado.")
        return produto
