from rest_framework.serializers import ModelSerializer

from solutions.models import  Cliente, Funcionario, Ferramenta, ItemEstoque, Celular, Caixa

class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"

class FuncionarioSerializer(ModelSerializer):
    class Meta:
        model = Funcionario
        fields = "__all__"

class FerramentaSerializer(ModelSerializer):
    class Meta:
        model = Ferramenta
        fields = "__all__"

class ItemEstoqueSerializer(ModelSerializer):
    class Meta:
        model = ItemEstoque
        fields = "__all__"

class CelularSerializer(ModelSerializer):
    class Meta:
        model = Celular
        fields = "__all__"

class CaixaSerializer(ModelSerializer):
    class Meta:
        model = Caixa 
        fields = "__all__"