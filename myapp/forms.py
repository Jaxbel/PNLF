from django import forms
from .models import Jugadores

class JugadoresForm(forms.ModelForm):
    class Meta:
        model = Jugadores
        fields = '__all__'