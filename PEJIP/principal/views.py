from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# librerias del crud
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#importo el modelo de la base de datos de models.py
from .models import *
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
 
# Habilitamos los formularios en Django
from django import forms


# Create your views here.
def FormularioContacto(request):
    return render(request, "FormularioContacto.html")

def indexprincipal(request):
    return render(request, "index.html")

def contactar(request):
    if request.method =="POST":
         asunto = request.POST["txtAsunto"]
         mensaje = request.POST["txtMensaje"] + "Email:" + request.POST["txtEmail"] 
         email_desde = settings.EMAIL_HOST_USER
         email_para = ["aanacona40@misena.edu.co"]
         send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)
         return render(request, "contactoExitoso.html")
    return render(request, "FormularioContacto.html")


class ListadoAntojos(ListView):
    model = Antojos
    
    
class AntojosCrear(SuccessMessageMixin, CreateView):
    model =Antojos
    form = Antojos
    fields = "__all__"
    success_message ='Antojos creada correctamente'
     
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class AntojosDetalle (DetailView):
    model =Antojos

class  AntojosActualizar(SuccessMessageMixin,UpdateView):
    model =  Antojos
    form = Antojos
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Antojos Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
class AntojosEliminar(SuccessMessageMixin, DeleteView): 
    model = Antojos 
    form = Antojos
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Antojos Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer

