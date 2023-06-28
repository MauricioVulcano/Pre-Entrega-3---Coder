from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from NuevaApp.models import *
from NuevaApp.forms import *





def inicio(request):
    return render(request, "NuevaApp/inicio.html")

def usuarios(request):
    return render(request, "NuevaApp/usuarios.html")

def setUsuarios(request):
    return render(request, "NuevaApp/setUsuarios.html")

def juegos(request):
    return render(request, "NuevaApp/juegos.html")

def setJuegos(request):
    return render(request, "NuevaApp/setJuegos.html")

def getJuegos(request):
    return render(request, "NuevaApp/getJuegos.html")

def perifericos(request):
    return render(request, "NuevaApp/perifericos.html")

def setPerifericos(request):
    return render(request, "NuevaApp/setPerifericos.html")

def getPerifericos(request):
    return render(request, "NuevaApp/getJuegos.html")



#Usuarios

def setUsuarios (request):
    if request.method == "POST":
        miFormulario1 = formSetUsuario(request.POST)
        print(miFormulario1)
        if miFormulario1.is_valid:
            dataUsuarios = miFormulario1.cleaned_data
            cargarUsuario = Usuario(nombre=dataUsuarios["nombre"], apellido=dataUsuarios["apellido"], email=dataUsuarios["email"])
            cargarUsuario.save()
            return render(request,"NuevaApp/inicio.html")
    else:
        miFormulario1 = formSetUsuario()
    
    return render(request,"NuevaApp/setUsuarios.html",{"miFormulario1":miFormulario1})

# Juegos

def setJuegos (request):
    if request.method == "POST":
        miFormulario2 = formSetListaJuegos(request.POST)
        print(miFormulario2)
        if miFormulario2.is_valid:
            dataProductos = miFormulario2.cleaned_data
            cargarProducto = listaJuegos(consola=dataProductos["consola"], juego=dataProductos["juego"], precio=dataProductos["precio"])
            cargarProducto.save()
            return render(request,"NuevaApp/inicio.html")
    else:
        miFormulario2 = formSetListaJuegos()
    
    return render(request,"NuevaApp/setJuegos.html",{"miFormulario2":miFormulario2})


def buscarJuego (request):
    if request.GET["juego"]:
        juego = request.GET["juego"]
        listaJuegos = listaJuegos.objects.filter(juego = juego)
        return render(request, "NuevaApp/getJuegos",{"juego":listaJuegos})
    else:
        respuesta = "No se enviaron juegos"

    return HttpResponse(respuesta)


# Perifericos

def setPerifericos (request):
    if request.method == "POST":
        miFormulario3 = formSetListaPerifericos(request.POST)
        print(miFormulario3)
        if miFormulario3.is_valid:
            dataPerifericos = miFormulario3.cleaned_data
            cargarPerifericos = listaJuegos(consola=dataPerifericos["consola"], juego=dataPerifericos["juego"], precio=dataPerifericos["precio"])
            cargarPerifericos.save()
            return render(request,"NuevaApp/inicio.html")
    else:
        miFormulario3 = formSetListaPerifericos()
    
    return render(request,"NuevaApp/setJuegos.html",{"miFormulario2":miFormulario3})


def buscarJuego (request):
    if request.GET["juego"]:
        juego = request.GET["juego"]
        listaJuegos = listaJuegos.objects.filter(juego = juego)
        return render(request, "NuevaApp/getJuegos",{"juego":listaJuegos})
    else:
        respuesta = "No se enviaron juegos"

    return HttpResponse(respuesta)



    





