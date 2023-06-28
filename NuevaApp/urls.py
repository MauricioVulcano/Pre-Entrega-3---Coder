"""
URL configuration for PreEntrega3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from NuevaApp.views import *

urlpatterns = [
    path('inicio/', inicio, name = "inicio"),
    path('usuarios/',usuarios, name = "usuarios"),
    path('setUsuarios/', setUsuarios, name = "setUsuarios"),
    path('juegos/', juegos, name = "juegos"),
    path('setJuegos/', setJuegos, name = "setJuegos"),
    path('getJuegos/', buscarJuego, name = "getJuegos"),
    path('perifericos/', perifericos, name = "perifericos"),
    path('setPerifericos/', setPerifericos, name = "setPerifericos"),
    path('getPerifericos/', getPerifericos, name = "getPerifericos"),
   
]
