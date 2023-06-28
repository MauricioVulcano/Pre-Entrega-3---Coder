from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    #path('',saludo), #si lo ponemos asi es una pagina por default
    path('admin/', admin.site.urls),
    path('NuevaApp/',include('NuevaApp.urls')),

]
