"""PEJIP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from principal.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('FormularioContacto/', FormularioContacto),
    path('contactar/', contactar),
    path('index/', indexprincipal),
    path('Antojos/', ListadoAntojos.as_view(template_name = "Antojos/index.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Antojos o registro 
    path('Antojos/detalle/<int:pk>', AntojosDetalle.as_view(template_name = "Antojos/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Antojos o registro  
    path('Antojos/crear', AntojosCrear.as_view(template_name = "Antojos/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Antojoso registro de la Base de Datos 
    path('Antojos/editar/<int:pk>', AntojosActualizar.as_view(template_name = "Antojos/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Antojos o registro de la Base de Datos 
    path('Antojos/eliminar/<int:pk>', AntojosEliminar.as_view(), name='Antojos/eliminar.html'),    
]
   
