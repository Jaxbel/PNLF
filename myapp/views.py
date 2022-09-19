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
    if request.method == 'POST':
       if formulario.is_valid():
            formulario.save()
            formulario = JugadoresForm()

    return render(request, 'jugadores/crear.html', {'formulario': formulario})

# Editar
def editar_jugador(request, id):
    jugador=Jugadores.objects.get(id=id)
    if request.method== 'GET':       
        formulario = JugadoresForm(initial=jugador.__dict__)

    if request.method == 'POST':
       formulario = JugadoresForm(request.POST, initial=jugador.__dict__)
       if formulario.is_valid():
            formulario.save(commit=False)
            jugador.nombre = formulario.cleaned_data['nombre']
            jugador.numero_playera = formulario.cleaned_data['numero_playera']
            jugador.edad = formulario.cleaned_data['edad']
            jugador.equipo = formulario.cleaned_data['equipo']
            jugador.posicion = formulario.cleaned_data['posicion']
            jugador.estadio = formulario.cleaned_data['estadio']
            jugador.save()

    return render(request, 'jugadores/editar.html', {'formulario': formulario})


def eliminar_jugador(request,id):
    jugador=Jugadores.objects.filter(id=id).first()
    jugador.delete()
    jugadores=Jugadores.objects.all()
    return render(request, 'jugadores/index.html', {'jugadores':jugadores})
