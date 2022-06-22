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








# Create your views here.
def FormularioContacto(request):
    return render(request, "FormularioContacto.html")

def informacion(request):
    return render(request, "informacion.html")

def registro(request):
    return render(request, "registro2.html")   

def registro1(request):
    return render(request, "registro1.html")

def anticonceptivos2(request):
    return render(request, "anticonceptivos2.html")

def mestrual(request):
    return render(request, "menstrual.html")

def menstrual2(request):
    return render(request, "menstrual2.html")

def calendariop(request):
    return render(request, "CalendarioP.html")

def funciones(request):
    return render(request, "Funciones_Calendario.html")        

def cartelera(request):
    return render(request, "cartelera.html")

def psicologia(request):
    return render(request, "psicologia.html")

def entidades(request):
    return render(request, "entidades.html")    
                                 
def cita(request):
    return render(request, "cita.html")                                  

def indexprincipal(request):
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")    


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
        return reverse('leerA') # Redireccionamos a la vista principal 'leerA'

class AntojosDetalle (DetailView):
    model =Antojos

class  AntojosActualizar(SuccessMessageMixin,UpdateView):
    model =  Antojos
    form = Antojos
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Antojos Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('leerA') # Redireccionamos a la vista principal 'leerA'
class AntojosEliminar(SuccessMessageMixin, DeleteView): 
    model = Antojos 
    form = Antojos
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Antojos Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leerA') # Redireccionamos a la vista principal 'leerA'


class ListadoDepartamento(ListView):
    model = Departamento
    
    
class DepartamentoCrear(SuccessMessageMixin, CreateView):
    model =Departamento
    form = Departamento
    fields = "__all__"
    success_message ='Departamento creada correctamente'
     
    def get_success_url(self):        
        return reverse('leerD') # Redireccionamos a la vista principal 'leerD'
 
class DepartamentoDetalle (DetailView):
    model =Departamento
 
class  DepartamentoActualizar(SuccessMessageMixin,UpdateView):
    model =  Departamento
    form = Departamento
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Departamento Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    def get_success_url(self):               
        return reverse('leerD') # Redireccionamos a la vista principal 'leerD'
class DepartamentoEliminar(SuccessMessageMixin, DeleteView): 
    model = Departamento 
    form = Departamento
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Departamento Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leerD') # Redireccionamos a la vista principal 'leerD'



class ListadoEventos(ListView):
    model = Eventos
    
    
class EventosCrear(SuccessMessageMixin, CreateView):
    model =Eventos
    form = Eventos
    fields = "__all__"
    success_message ='Eventos creada correctamente'
     
    def get_success_url(self):        
        return reverse('leerE') # Redireccionamos a la vista principal 'leerE'
 
class EventosDetalle (DetailView):
    model =Eventos
 
class  EventosActualizar(SuccessMessageMixin,UpdateView):
    model =  Eventos
    form = Eventos
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Eventos Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    def get_success_url(self):               
        return reverse('leerE') # Redireccionamos a la vista principal 'leerE'
class EventosEliminar(SuccessMessageMixin, DeleteView): 
    model = Eventos 
    form = Eventos
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Eventos Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leerE') # Redireccionamos a la vista principal 'leerE'



class ListadoGenero(ListView):
    model = Genero
    
    
class GeneroCrear(SuccessMessageMixin, CreateView):
    model =Genero
    form = Genero
    fields = "__all__"
    success_message ='Genero creada correctamente'
     
    def get_success_url(self):        
        return reverse('leerG') # Redireccionamos a la vista principal 'leerG'
 
class GeneroDetalle (DetailView):
    model =Genero
 
class  GeneroActualizar(SuccessMessageMixin,UpdateView):
    model =  Genero
    form = Genero
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Genero Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    def get_success_url(self):               
        return reverse('leerG') # Redireccionamos a la vista principal 'leerG'
class GeneroEliminar(SuccessMessageMixin, DeleteView): 
    model = Genero 
    form = Genero
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Genero Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leerG') # Redireccionamos a la vista principal 'leerG'



class ListadoMedicamentos(ListView):
    model = Medicamentos
    
    
class MedicamentosCrear(SuccessMessageMixin, CreateView):
    model =Medicamentos
    form = Medicamentos
    fields = "__all__"
    success_message ='Medicamentos creada correctamente'
     
    def get_success_url(self):        
        return reverse('leerM') # Redireccionamos a la vista principal 'leerM'
 
class MedicamentosDetalle (DetailView):
    model =Medicamentos
 
class  MedicamentosActualizar(SuccessMessageMixin,UpdateView):
    model =  Medicamentos
    form = Medicamentos
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Medicamentos Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    def get_success_url(self):               
        return reverse('leerM') # Redireccionamos a la vista principal 'leerM'
class MedicamentosEliminar(SuccessMessageMixin, DeleteView): 
    model = Medicamentos 
    form = Medicamentos
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Medicamentos Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leerM') # Redireccionamos a la vista principal 'leerM'




class ListadoTipodocumento(ListView):
    model = Tipodocumento
    
    
class TipodocumentoCrear(SuccessMessageMixin, CreateView):
    model =Tipodocumento
    form = Tipodocumento
    fields = "__all__"
    success_message ='Tipodocumento creada correctamente'
     
    def get_success_url(self):        
        return reverse('leerTD') # Redireccionamos a la vista principal 'leerTD'
 
class TipodocumentoDetalle (DetailView):
    model =Tipodocumento
 
class  TipodocumentoActualizar(SuccessMessageMixin,UpdateView):
    model =  Tipodocumento
    form = Tipodocumento
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Tipodocumento Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    def get_success_url(self):               
        return reverse('leerTD') # Redireccionamos a la vista principal 'leerTD'
class TipodocumentoEliminar(SuccessMessageMixin, DeleteView): 
    model = Tipodocumento 
    form = Tipodocumento
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Tipodocumento Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leerTD') # Redireccionamos a la vista principal 'leerTD'





class ListadoMetodoanticonceptivo(ListView):
    model = Metodoanticonceptivo
    
    
class MetodoanticonceptivoCrear(SuccessMessageMixin, CreateView):
    model =Metodoanticonceptivo
    form = Metodoanticonceptivo
    fields = "__all__"
    success_message ='Metodoanticonceptivo creada correctamente'
     
    def get_success_url(self):        
        return reverse('leerMA') # Redireccionamos a la vista principal 'leerMA'
 
class MetodoanticonceptivoDetalle (DetailView):
    model =Metodoanticonceptivo
 
class  MetodoanticonceptivoActualizar(SuccessMessageMixin,UpdateView):
    model =  Metodoanticonceptivo
    form = Metodoanticonceptivo
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Metodoanticonceptivo Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    def get_success_url(self):               
        return reverse('leerMA') # Redireccionamos a la vista principal 'leerMA'
class MetodoanticonceptivoEliminar(SuccessMessageMixin, DeleteView): 
    model = Metodoanticonceptivo 
    form = Metodoanticonceptivo
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Metodoanticonceptivo Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leerMA') # Redireccionamos a la vista principal 'leerMA'




class ListadoTipoperiodo(ListView):
    model = Tipoperiodo
    
    
class TipoperiodoCrear(SuccessMessageMixin, CreateView):
    model =Tipoperiodo
    form = Tipoperiodo
    fields = "__all__"
    success_message ='Tipoperiodo creada correctamente'
     
    def get_success_url(self):        
        return reverse('leerTP') # Redireccionamos a la vista principal 'leerTP'
 
class TipoperiodoDetalle (DetailView):
    model =Tipoperiodo
 
class  TipoperiodoActualizar(SuccessMessageMixin,UpdateView):
    model =  Tipoperiodo
    form = Tipoperiodo
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Tipoperiodo Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    def get_success_url(self):               
        return reverse('leerTP') # Redireccionamos a la vista principal 'leerTP'
class TipoperiodoEliminar(SuccessMessageMixin, DeleteView): 
    model = Tipoperiodo 
    form = Tipoperiodo
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Tipoperiodo Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leerTP') # Redireccionamos a la vista principal 'leerTP'




class ListadoEmpresa(ListView):
    model = Empresa
    
    
class EmpresaCrear(SuccessMessageMixin, CreateView):
    model =Empresa
    form = Empresa
    fields = "__all__"
    success_message ='Empresa creada correctamente'
     
    def get_success_url(self):        
        return reverse('leerEm') # Redireccionamos a la vista principal 'leerEm'
 
class EmpresaDetalle (DetailView):
    model =Empresa
 
class  EmpresaActualizar(SuccessMessageMixin,UpdateView):
    model =  Empresa
    form = Empresa
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Empresa Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    def get_success_url(self):               
        return reverse('leerEm') # Redireccionamos a la vista principal 'leerEm'
class EmpresaEliminar(SuccessMessageMixin, DeleteView): 
    model = Empresa 
    form = Empresa
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Empresa Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leerEm') # Redireccionamos a la vista principal 'leerEm'




class ListadoExamen(ListView):
    model = Examen
    
    
class ExamenCrear(SuccessMessageMixin, CreateView):
    model =Examen
    form = Examen
    fields = "__all__"
    success_message ='Examen creada correctamente'
     
    def get_success_url(self):        
        return reverse('leerEx') # Redireccionamos a la vista principal 'leerEx'
 
class ExamenDetalle (DetailView):
    model =Examen
 
class  ExamenActualizar(SuccessMessageMixin,UpdateView):
    model =  Examen
    form = Examen
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Examen Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    def get_success_url(self):               
        return reverse('leerEx') # Redireccionamos a la vista principal 'leerEx'
class ExamenEliminar(SuccessMessageMixin, DeleteView): 
    model = Examen 
    form = Examen
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Examen Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leerEx') # Redireccionamos a la vista principal 'leerEx'




class ListadoLugarnacimiento(ListView):
    model = Lugarnacimiento
    
    
class LugarnacimientoCrear(SuccessMessageMixin, CreateView):
    model =Lugarnacimiento
    form = Lugarnacimiento
    fields = "__all__"
    success_message ='Lugarnacimiento creada correctamente'
     
    def get_success_url(self):        
        return reverse('leerL') # Redireccionamos a la vista principal 'leerL'
 
class LugarnacimientoDetalle (DetailView):
    model =Lugarnacimiento
 
class  LugarnacimientoActualizar(SuccessMessageMixin,UpdateView):
    model =  Lugarnacimiento
    form = Lugarnacimiento
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Lugarnacimiento Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    def get_success_url(self):               
        return reverse('leerL') # Redireccionamos a la vista principal 'leerL'
class LugarnacimientoEliminar(SuccessMessageMixin, DeleteView): 
    model = Lugarnacimiento 
    form = Lugarnacimiento
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Lugarnacimiento Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leerL') # Redireccionamos a la vista principal 'leerL'






class ListadoMunicipio(ListView):
    model = Municipio
    
    
class MunicipioCrear(SuccessMessageMixin, CreateView):
    model =Municipio
    form = Municipio
    fields = "__all__"
    success_message ='Municipio creada correctamente'
     
    def get_success_url(self):        
        return reverse('leerMu') # Redireccionamos a la vista principal 'leerMu'
 
class MunicipioDetalle (DetailView):
    model =Municipio
 
class  MunicipioActualizar(SuccessMessageMixin,UpdateView):
    model =  Municipio
    form = Municipio
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Municipio Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    def get_success_url(self):               
        return reverse('leerMu') # Redireccionamos a la vista principal 'leerMu'
class MunicipioEliminar(SuccessMessageMixin, DeleteView): 
    model = Municipio 
    form = Municipio
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Municipio Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leerMu') # Redireccionamos a la vista principal 'leerMu'



class ListadoPersonacontacto(ListView):
    model = Personacontacto
    
    
class PersonacontactoCrear(SuccessMessageMixin, CreateView):
    model =Personacontacto
    form = Personacontacto
    fields = "__all__"
    success_message ='Personacontacto creada correctamente'
     
    def get_success_url(self):        
        return reverse('leerPC') # Redireccionamos a la vista principal 'leerPC'
 
class PersonacontactoDetalle (DetailView):
    model =Personacontacto
 
class  PersonacontactoActualizar(SuccessMessageMixin,UpdateView):
    model =  Personacontacto
    form = Personacontacto
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Personacontacto Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    def get_success_url(self):               
        return reverse('leerPC') # Redireccionamos a la vista principal 'leerPC'
class PersonacontactoEliminar(SuccessMessageMixin, DeleteView): 
    model = Personacontacto 
    form = Personacontacto
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Personacontacto Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leerPC') # Redireccionamos a la vista principal 'leerPC'



class ListadoSintomas(ListView):
    model = Sintomas
    
    
class SintomasCrear(SuccessMessageMixin, CreateView):
    model =Sintomas
    form = Sintomas
    fields = "__all__"
    success_message ='Sintomas creada correctamente'
     
    def get_success_url(self):        
        return reverse('leerS') # Redireccionamos a la vista principal 'leerS'
 
class SintomasDetalle (DetailView):
    model =Sintomas
 
class  SintomasActualizar(SuccessMessageMixin,UpdateView):
    model =  Sintomas
    form = Sintomas
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Sintomas Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    def get_success_url(self):               
        return reverse('leerS') # Redireccionamos a la vista principal 'leerS'
class SintomasEliminar(SuccessMessageMixin, DeleteView): 
    model = Sintomas 
    form = Sintomas
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Sintomas Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leerS') # Redireccionamos a la vista principal 'leerS'



class ListadoTipopersona(ListView):
    model = Tipopersona
    
    
class TipopersonaCrear(SuccessMessageMixin, CreateView):
    model =Tipopersona
    form = Tipopersona
    fields = "__all__"
    success_message ='Tipopersona creada correctamente'
     
    def get_success_url(self):        
        return reverse('leerTPe') # Redireccionamos a la vista principal 'leerTPe'
 
class TipopersonaDetalle (DetailView):
    model =Tipopersona
 
class  TipopersonaActualizar(SuccessMessageMixin,UpdateView):
    model =  Tipopersona
    form = Tipopersona
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Tipopersona Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    def get_success_url(self):               
        return reverse('leerTPe') # Redireccionamos a la vista principal 'leerTPe'
class TipopersonaEliminar(SuccessMessageMixin, DeleteView): 
    model = Tipopersona 
    form = Tipopersona
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Tipopersona Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leerTPe') # Redireccionamos a la vista principal 'leerTPe'



class ListadoTiposangre(ListView):
    model = Tiposangre
    
    
class TiposangreCrear(SuccessMessageMixin, CreateView):
    model =Tiposangre
    form = Tiposangre
    fields = "__all__"
    success_message ='Tiposangre creada correctamente'
     
    def get_success_url(self):        
        return reverse('leerTS') # Redireccionamos a la vista principal 'leer'
 
class TiposangreDetalle (DetailView):
    model =Tiposangre
 
class  TiposangreActualizar(SuccessMessageMixin,UpdateView):
    model =  Tiposangre
    form = Tiposangre
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Tiposangre Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    def get_success_url(self):               
        return reverse('leerTS') # Redireccionamos a la vista principal 'leerTs'
class TiposangreEliminar(SuccessMessageMixin, DeleteView): 
    model = Tiposangre 
    form = Tiposangre
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Tiposangre Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leerTS') # Redireccionamos a la vista principal 'leerTs'




class ListadoTiposervicio(ListView):
    model = Tiposervicio
    
    
class TiposervicioCrear(SuccessMessageMixin, CreateView):
    model =Tiposervicio
    form = Tiposervicio
    fields = "__all__"
    success_message ='Tiposervicio creada correctamente'
     
    def get_success_url(self):        
        return reverse('leerTSe') # Redireccionamos a la vista principal 'leerTSe'
 
class TiposervicioDetalle (DetailView):
    model =Tiposervicio
 
class  TiposervicioActualizar(SuccessMessageMixin,UpdateView):
    model =  Tiposervicio
    form = Tiposervicio
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Tiposervicio Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    def get_success_url(self):               
        return reverse('leerTSe') # Redireccionamos a la vista principal 'leerTSe'
class TiposervicioEliminar(SuccessMessageMixin, DeleteView): 
    model = Tiposervicio 
    form = Tiposervicio
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Tiposervicio Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leerTSe') # Redireccionamos a la vista principal 'leerTSe'