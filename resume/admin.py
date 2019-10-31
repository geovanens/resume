from django.contrib import admin

# Register your models here.

from .models import Profissional, Perfil, Tecnologia, Formacao, Academico

class PerfilAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')

class ProfissionalAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'cargo', 'nome_empresa')

class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria')

class FormacaoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'nome_instituicao')

class AcademicoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao')

admin.site.register(Perfil, PerfilAdmin)
admin.site.register(Profissional, ProfissionalAdmin)
admin.site.register(Tecnologia, TecnologiaAdmin)
admin.site.register(Formacao, FormacaoAdmin)
admin.site.register(Academico, AcademicoAdmin)