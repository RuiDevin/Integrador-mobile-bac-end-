from django.contrib import admin

from .models import Caixa, Cliente, Ferramenta, Funcionario, ItemEstoque, Celular

admin.site.register(Ferramenta)
admin.site.register(Funcionario)
admin.site.register(Cliente)
admin.site.register(Caixa)
admin.site.register(ItemEstoque)
admin.site.register(Celular)
