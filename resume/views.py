from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime, date

from .models import Perfil, Profissional, Academico

# Create your views here.

def index(request):
    obj = Perfil.objects.all()[0]
    context = {'data': obj}
    print("Index", context['data'].foto)
    return render(request, 'resume/index.html', context)

def perfil(request):
    obj = Perfil.objects.all()[0]
    hoje = datetime.now()
    formatado = date(hoje.year, hoje.month, hoje.day)
    idade = abs(formatado - obj.nascimento).days//365
    context = {'data': obj, 'idade': idade}
    return render(request, 'resume/perfil.html', context)

def profissional(request):
    obj = Profissional.objects.all()
    context = {'data': obj}
    return render(request, 'resume/profissional.html', context)

def academico(request):
    obj = Academico.objects.all()
    context = {'data': obj}
    return render(request, 'resume/academico.html', context)
