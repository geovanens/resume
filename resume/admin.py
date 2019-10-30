from django.contrib import admin

# Register your models here.

from .models import Profissional, Perfil

admin.site.register(Profissional)
admin.site.register(Perfil)