from django.contrib import admin
from .models import Categoria, Produto

# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass
    list_filter = ('nome',)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    pass
    list_display = ('nome', 'preco', 'descricao', 'categoria')
    list_filter = ('categoria',)
