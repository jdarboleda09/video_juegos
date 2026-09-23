from django.contrib import admin
from .models import Consola


@admin.register(Consola)
class ConsolaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'cantidad', 'precio_dia')
    list_filter = ('tipo',)