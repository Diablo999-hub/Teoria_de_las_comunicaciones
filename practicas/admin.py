from django.contrib import admin
from .models import Practica

@admin.register(Practica)
class PracticaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'objetivo')
    prepopulated_fields = {"slug": ("titulo",)}
    search_fields = ('titulo', 'objetivo', 'contenido_html')

