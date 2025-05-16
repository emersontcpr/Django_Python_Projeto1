
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from Loja.views import ClienteViewSet, VendedorViewSet, ProdutoViewSet, UnicoProdutoViewSet, UnicoClienteViewSet, UnicoVendedorViewSet, ListarProdutoPorVendedorViewSet


router = routers.DefaultRouter()
router.register('clientes', ClienteViewSet, basename='Clientes')
router.register('vendedores', VendedorViewSet, basename='Vendedores')
router.register('produtos', ProdutoViewSet, basename='Produtos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('produtos/listarTodos/<int:id>',
         ListarProdutoPorVendedorViewSet.as_view())
]
