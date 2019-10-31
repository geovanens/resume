from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('perfil', views.perfil, name='perfil'),
    path('profissional', views.profissional, name='profissional'),
    path('academico', views.academico, name='academico'),
]