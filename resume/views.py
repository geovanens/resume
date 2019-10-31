from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime, date

from .models import Perfil, Profissional, Academico

# Create your views here.

def index(request):
    foto = Perfil.objects.all()[0].foto
    context = {'foto': foto}
    return render(request, 'resume/index.html', context)

def perfil(request):
    print(request)
    obj = Perfil.objects.all()[0]
    foto = obj.foto
    hoje = datetime.now()
    formatado = date(hoje.year, hoje.month, hoje.day)
    idade = abs(formatado - obj.nascimento).days//365
    context = {'data': obj, 'idade': idade, 'foto': foto}
    return render(request, 'resume/perfil.html', context)

def profissional(request):
    foto = Perfil.objects.all()[0].foto
    obj = Profissional.objects.all()
    context = {'data': obj, 'foto': foto}
    return render(request, 'resume/profissional.html', context)

def academico(request):
    obj = Academico.objects.all()
    foto = Perfil.objects.all()[0].foto
    context = {'data': obj, 'foto': foto}
    return render(request, 'resume/academico.html', context)
