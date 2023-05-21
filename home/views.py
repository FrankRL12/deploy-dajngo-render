from django.shortcuts import render

# Create your views here.


def inicio(request):
    return render(request , 'inicio.html')


def temporada(request):
    return render(request, 'temporada.html')

def descarga(request):
    return render(request, 'descarga.html')


def bloc(request):
    return render(request, 'bloc.html')


def contacto(request):
    return render(request, 'contacto.html') 