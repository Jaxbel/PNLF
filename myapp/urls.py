from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('jugadores', views.jugadores, name='jugadores'),   
    path('nosotros', views.nosotros, name='nosotros'),
    path('jugadores/crear', views.crear_jugador, name='crear'),
    path('jugadores/editar', views.editar_jugador, name='editar'),
    
    
]