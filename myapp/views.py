from django.http import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')
def jugadores(request):
    return render(request, 'jugadores/index.html')
def crear_jugador(request):
    return render(request, 'jugadores/crear.html')
def editar_jugador(request):
    return render(request, 'jugadores/editar.html')
