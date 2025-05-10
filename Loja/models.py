import uuid
from django.db import models
from django.core.validators import MinLengthValidator


class Cliente(models.Model):
    nome = models.CharField(max_length=20, blank=False, null=False)
    sobrenome = models.CharField(max_length=20, blank=False, null=False,)
    email = models.EmailField(blank=False, max_length=30, unique=True)
    cpf = models.CharField(max_length=14, blank=False, null=False, unique=True,
                           validators=[MinLengthValidator(11, "O CPF do cliente é inválido!")])
    login = models.CharField(
        max_length=15, blank=False, null=False, unique=True)
    senha = models.CharField(max_length=12, blank=False, null=False,
                             validators=[MinLengthValidator(8, "O Senha do cliente  é inválida!"),])
    guid = models.CharField(max_length=50, blank=False,
                            null=False, default=uuid.uuid4, unique=True)

    def __str__(self):
        return self.nome


class Vendedor(models.Model):
    nome = models.CharField(max_length=20, blank=False, null=False)
    sobrenome = models.CharField(max_length=20, blank=False, null=False,)
    email = models.EmailField(blank=False, max_length=30, unique=True)
    cnpj = models.CharField(max_length=19, blank=False, null=False, unique=True,
                            validators=[MinLengthValidator(14, "O cnpj do vendedor é inválido!")])
    nomeComercial = models.CharField(max_length=50, blank=False, null=False,)
    login = models.CharField(
        max_length=15, blank=False, null=False, unique=True)
    senha = models.CharField(max_length=12, blank=False, null=False,
                             validators=[MinLengthValidator(8, "O Senha do cliente  é inválida!"),])
    guid = models.CharField(max_length=50, blank=False,
                            null=False, default=uuid.uuid4, unique=True)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=30, blank=False, null=False)
    descricao = models.CharField(max_length=100, blank=False, null=False,)
    valor = models.DecimalField(
        max_digits=10, decimal_places=2, blank=False, null=False)
    quantidade = models.IntegerField(blank=False, null=False)
    categoria = models.CharField(blank=False, null=False,)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    guid = models.CharField(max_length=50, blank=False,
                            null=False, default=uuid.uuid4, unique=True)

    def __str__(self):
        return self.nome
