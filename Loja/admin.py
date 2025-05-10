from django.contrib import admin
from .models import Cliente, Vendedor, Produto


class Clientes(admin.ModelAdmin):
    list_display = ('guid', 'nome', 'login')
    list_display_links = ('guid', 'nome',)
    list_per_page = 20
    search_fields = ('cpf',)
    fields = ('nome', 'sobrenome', 'email', 'cpf', 'login', 'senha')

    def get_readonly_fields(self, request, obj=None):
        if obj:  # se estiver editando
            return ('guid', 'email', 'cpf', 'login')
        return ('guid')  # nenhum campo é readonly na criação


admin.site.register(Cliente, Clientes)


class Vendedores(admin.ModelAdmin):
    list_display = ('guid', 'nome', 'login')
    list_display_links = ('guid', 'nome',)
    list_per_page = 20
    search_fields = ('cnpj',)
    fields = ('nome', 'sobrenome', 'email',
              'nomeComercial', 'cnpj', 'login', 'senha')

    def get_readonly_fields(self, request, obj=None):
        if obj:  # se estiver editando
            return ('guid', 'email', 'cnpj', 'login')
        return ('guid')  # nenhum campo é readonly na criação


admin.site.register(Vendedor, Vendedores)


class Produtos(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'valor', 'quantidade')
    list_display_links = ('nome',)
    list_per_page = 20
    search_fields = ('categoria',)
    fields = ('nome', 'descricao', 'valor',
              'quantidade', 'categoria', 'vendedor')

    def get_readonly_fields(self, request, obj=None):
        if obj:  # se estiver editando
            return ('guid', 'vendedor')
        return ('guid')  # nenhum campo é readonly na criação


admin.site.register(Produto, Produtos)
