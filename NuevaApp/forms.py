from django import forms

class formSetUsuario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()

class formSetListaJuegos(forms.Form):
    consola = forms.CharField(max_length=30)
    juego = forms.CharField(max_length=30)
    precio = forms.CharField(max_length=30)

class formSetListaPerifericos (forms.Form):
    consola = forms.CharField(max_length=30)
    periferico = forms.CharField(max_length=30)
    precio = forms.CharField(max_length=30)
