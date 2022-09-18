from django.http import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse
from .models import Jugadores
from .forms import JugadoresForm

# Create your views here.
def inicio(request):
    return render(request, 'paginas/inicio.html')
# Nosotros
def nosotros(request):
    return render(request, 'paginas/nosotros.html')
# Jugadores
def jugadores(request):
    jugadores=Jugadores.objects.all()
    return render(request, 'jugadores/index.html', {'jugadores':jugadores})
# Crear
def crear_jugador(request):
    formulario = JugadoresForm(request.POST or None)
    return render(request, 'jugadores/crear.html', {'formulario': formulario})
# Editar
def editar_jugador(request):
    return render(request, 'jugadores/editar.html')
