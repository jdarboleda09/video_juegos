from django.shortcuts import render
from .models import Consola


def inicio(request):
    consolas = Consola.objects.all()

    return render(request, 'alquiler/inicio.html', {
        'consolas': consolas
    })