from rest_framework.viewsets import ModelViewSet

from solutions.models import Cliente, Funcionario, Ferramenta, ItemEstoque, Celular, Caixa
from solutions.serializers import ClienteSerializer, FuncionarioSerializer, FerramentaSerializer, ItemEstoqueSerializer, CelularSerializer, CaixaSerializer

class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class FuncionarioViewSet(ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class FerramentaViewSet(ModelViewSet):
    queryset = Ferramenta.objects.all()
    serializer_class = FerramentaSerializer

class ItemEstoqueViewSet(ModelViewSet):
    queryset = ItemEstoque.objects.all()
    serializer_class = ItemEstoqueSerializer

class CelularViewSet(ModelViewSet):
    queryset = Celular.objects.all()
    serializer_class = CelularSerializer

class CaixaViewSet(ModelViewSet):
    queryset = Caixa.objects.all()
    serializer_class = CaixaSerializer