from django.contrib import admin

# Register your models here.

from .models import Profissional, Perfil

class PerfilAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')

class ProfissionalAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'cargo', 'nome_empresa')

admin.site.register(Perfil, PerfilAdmin)
admin.site.register(Profissional, ProfissionalAdmin)