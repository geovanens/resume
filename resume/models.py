from django.db import models

# Create your models here.

class Profissional(models.Model):
    tipo = models.CharField(max_length=200)
    logo_empresa = models.URLField()
    cargo = models.CharField(max_length=200)
    nome_empresa = models.CharField(max_length=200)
    inicio = models.DateField()
    fim = models.DateField()
    descricao = models.TextField()
    tecnologias = models.TextField()

class Perfil(models.Model):
    foto = models.URLField()
    nome = models.CharField(max_length=200)
    nascimento = models.DateField()
    telefone = models.CharField(max_length=200)
    email = models.EmailField()
    endereco = models.CharField(max_length=200)
    celular = models.CharField(max_length=200)
    linkedin = models.URLField()
    github = models.URLField()
    descricao = models.TextField()