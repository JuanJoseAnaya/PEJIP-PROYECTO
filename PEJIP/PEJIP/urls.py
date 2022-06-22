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
    path('informacion/', informacion),
    path('registro2/', registro),
    path('registro1/', registro1),
    path('anticonceptivos2/', anticonceptivos2),
    path('mestrual/', mestrual),
    path('menstrual2/', menstrual2),
    path('calendariop/', calendariop),
    path('funciones/', funciones),
    path('cartelera/', cartelera),
    path('psicologia/', psicologia),
    path('entidades/', entidades),
    path('cita/', cita),
    path('index/', indexprincipal),
    path('login/', login),
    path('Antojos/', ListadoAntojos.as_view(template_name = "Antojos/index.html"), name='leerA'),
    path('Departamento/', ListadoDepartamento.as_view(template_name = "Departamento/index.html"), name='leerD'),
    path('Eventos/', ListadoEventos.as_view(template_name = "Eventos/index.html"), name='leerE'),
    path('Genero/', ListadoGenero.as_view(template_name = "Genero/index.html"), name='leerG'),
    path('Medicamentos/', ListadoMedicamentos.as_view(template_name = "Medicamentos/index.html"), name='leerM'),
    path('Tipodocumento/', ListadoTipodocumento.as_view(template_name = "Tipodocumento/index.html"), name='leerTD'),
    path('Metodoanticonceptivo/', ListadoMetodoanticonceptivo.as_view(template_name = "Metodoanticonceptivo/index.html"), name='leerMA'),
    path('Tipoperiodo/', ListadoTipoperiodo.as_view(template_name = "Tipoperiodo/index.html"), name='leerTP'),
    path('Empresa/', ListadoEmpresa.as_view(template_name = "Empresa/index.html"), name='leerEm'),
    path('Examen/', ListadoExamen.as_view(template_name = "Examen/index.html"), name='leerEx'),
    path('Lugarnacimiento/', ListadoLugarnacimiento.as_view(template_name = "Lugarnacimiento/index.html"), name='leerL'),
    path('Municipio/', ListadoMunicipio.as_view(template_name = "Municipio/index.html"), name='leerMu'),
    path('Personacontacto/', ListadoPersonacontacto.as_view(template_name = "Personacontacto/index.html"), name='leerPC'),
    path('Sintomas/', ListadoSintomas.as_view(template_name = "Sintomas/index.html"), name='leerS'),
    path('Tipopersona/', ListadoTipopersona.as_view(template_name = "Tipopersona/index.html"), name='leerTPe'),
    path('Tiposangre/', ListadoTiposangre.as_view(template_name = "Tiposangre/index.html"), name='leerTS'),
    path('Tiposervicio/', ListadoTiposervicio.as_view(template_name = "Tiposervicio/index.html"), name='leerTSe'),



    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Antojos o registro 
    path('Antojos/detalle/<int:pk>', AntojosDetalle.as_view(template_name = "Antojos/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Antojos o registro  
    path('Antojos/crear', AntojosCrear.as_view(template_name = "Antojos/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Antojoso registro de la Base de Datos 
    path('Antojos/editar/<int:pk>', AntojosActualizar.as_view(template_name = "Antojos/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Antojos o registro de la Base de Datos 
    path('Antojos/eliminar/<int:pk>', AntojosEliminar.as_view(), name='Antojos/eliminar.html'), 


    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Departamento o registro 
    path('Departamento/detalle/<int:pk>', DepartamentoDetalle.as_view(template_name = "Departamento/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Departamento o registro  
    path('Departamento/crear', DepartamentoCrear.as_view(template_name = "Departamento/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Departamentoo registro de la Base de Datos 
    path('Departamento/editar/<int:pk>', DepartamentoActualizar.as_view(template_name = "Departamento/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Departamento o registro de la Base de Datos 
    path('Departamento/eliminar/<int:pk>', DepartamentoEliminar.as_view(), name='Departamento/eliminar.html'),



    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Eventos o registro 
    path('Eventos/detalle/<int:pk>', EventosDetalle.as_view(template_name = "Eventos/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Eventos o registro  
    path('Eventos/crear', EventosCrear.as_view(template_name = "Eventos/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Eventoso registro de la Base de Datos 
    path('Eventos/editar/<int:pk>', EventosActualizar.as_view(template_name = "Eventos/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Eventos o registro de la Base de Datos 
    path('Eventos/eliminar/<int:pk>', EventosEliminar.as_view(), name='Eventos/eliminar.html'),



    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Genero o registro 
    path('Genero/detalle/<int:pk>', GeneroDetalle.as_view(template_name = "Genero/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Genero o registro  
    path('Genero/crear', GeneroCrear.as_view(template_name = "Genero/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Generoo registro de la Base de Datos 
    path('Genero/editar/<int:pk>', GeneroActualizar.as_view(template_name = "Genero/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Genero o registro de la Base de Datos 
    path('Genero/eliminar/<int:pk>', GeneroEliminar.as_view(), name='Genero/eliminar.html'),



    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Medicamentos o registro 
    path('Medicamentos/detalle/<int:pk>', MedicamentosDetalle.as_view(template_name = "Medicamentos/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Medicamentos o registro  
    path('Medicamentos/crear', MedicamentosCrear.as_view(template_name = "Medicamentos/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Medicamentoso registro de la Base de Datos 
    path('Medicamentos/editar/<int:pk>', MedicamentosActualizar.as_view(template_name = "Medicamentos/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Medicamentos o registro de la Base de Datos 
    path('Medicamentos/eliminar/<int:pk>', MedicamentosEliminar.as_view(), name='Medicamentos/eliminar.html'),




    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Tipodocumento o registro 
    path('Tipodocumento/detalle/<int:pk>', TipodocumentoDetalle.as_view(template_name = "Tipodocumento/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Tipodocumento o registro  
    path('Tipodocumento/crear', TipodocumentoCrear.as_view(template_name = "Tipodocumento/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Tipodocumentoo registro de la Base de Datos 
    path('Tipodocumento/editar/<int:pk>', TipodocumentoActualizar.as_view(template_name = "Tipodocumento/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Tipodocumento o registro de la Base de Datos 
    path('Tipodocumento/eliminar/<int:pk>', TipodocumentoEliminar.as_view(), name='Tipodocumento/eliminar.html'),



     # La ruta 'detalles' en donde mostraremos una página con los detalles de un Metodoanticonceptivo o registro 
    path('Metodoanticonceptivo/detalle/<int:pk>', MetodoanticonceptivoDetalle.as_view(template_name = "Metodoanticonceptivo/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Metodoanticonceptivo o registro  
    path('Metodoanticonceptivo/crear', MetodoanticonceptivoCrear.as_view(template_name = "Metodoanticonceptivo/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Metodoanticonceptivoo registro de la Base de Datos 
    path('Metodoanticonceptivo/editar/<int:pk>', MetodoanticonceptivoActualizar.as_view(template_name = "Metodoanticonceptivo/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Metodoanticonceptivo o registro de la Base de Datos 
    path('Metodoanticonceptivo/eliminar/<int:pk>', MetodoanticonceptivoEliminar.as_view(), name='Metodoanticonceptivo/eliminar.html'),



    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Tipoperiodo o registro 
    path('Tipoperiodo/detalle/<int:pk>', TipoperiodoDetalle.as_view(template_name = "Tipoperiodo/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Tipoperiodo o registro  
    path('Tipoperiodo/crear', TipoperiodoCrear.as_view(template_name = "Tipoperiodo/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Tipoperiodoo registro de la Base de Datos 
    path('Tipoperiodo/editar/<int:pk>', TipoperiodoActualizar.as_view(template_name = "Tipoperiodo/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Tipoperiodo o registro de la Base de Datos 
    path('Tipoperiodo/eliminar/<int:pk>', TipoperiodoEliminar.as_view(), name='Tipoperiodo/eliminar.html'),




    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Empresa o registro 
    path('Empresa/detalle/<int:pk>', EmpresaDetalle.as_view(template_name = "Empresa/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Empresa o registro  
    path('Empresa/crear', EmpresaCrear.as_view(template_name = "Empresa/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Empresao registro de la Base de Datos 
    path('Empresa/editar/<int:pk>', EmpresaActualizar.as_view(template_name = "Empresa/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Empresa o registro de la Base de Datos 
    path('Empresa/eliminar/<int:pk>', EmpresaEliminar.as_view(), name='Empresa/eliminar.html'),




    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Examen o registro 
    path('Examen/detalle/<int:pk>', ExamenDetalle.as_view(template_name = "Examen/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Examen o registro  
    path('Examen/crear', ExamenCrear.as_view(template_name = "Examen/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Exameno registro de la Base de Datos 
    path('Examen/editar/<int:pk>', ExamenActualizar.as_view(template_name = "Examen/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Examen o registro de la Base de Datos 
    path('Examen/eliminar/<int:pk>', ExamenEliminar.as_view(), name='Examen/eliminar.html'),




# La ruta 'detalles' en donde mostraremos una página con los detalles de un Lugarnacimiento o registro 
    path('Lugarnacimiento/detalle/<int:pk>', LugarnacimientoDetalle.as_view(template_name = "Lugarnacimiento/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Lugarnacimiento o registro  
    path('Lugarnacimiento/crear', LugarnacimientoCrear.as_view(template_name = "Lugarnacimiento/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Lugarnacimientoo registro de la Base de Datos 
    path('Lugarnacimiento/editar/<int:pk>', LugarnacimientoActualizar.as_view(template_name = "Lugarnacimiento/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Lugarnacimiento o registro de la Base de Datos 
    path('Lugarnacimiento/eliminar/<int:pk>', LugarnacimientoEliminar.as_view(), name='Lugarnacimiento/eliminar.html'),




# La ruta 'detalles' en donde mostraremos una página con los detalles de un Municipio o registro 
    path('Municipio/detalle/<int:pk>', MunicipioDetalle.as_view(template_name = "Municipio/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Municipio o registro  
    path('Municipio/crear', MunicipioCrear.as_view(template_name = "Municipio/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Municipioo registro de la Base de Datos 
    path('Municipio/editar/<int:pk>', MunicipioActualizar.as_view(template_name = "Municipio/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Municipio o registro de la Base de Datos 
    path('Municipio/eliminar/<int:pk>', MunicipioEliminar.as_view(), name='Municipio/eliminar.html'),




# La ruta 'detalles' en donde mostraremos una página con los detalles de un Personacontacto o registro 
    path('Personacontacto/detalle/<int:pk>', PersonacontactoDetalle.as_view(template_name = "Personacontacto/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Personacontacto o registro  
    path('Personacontacto/crear', PersonacontactoCrear.as_view(template_name = "Personacontacto/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Personacontactoo registro de la Base de Datos 
    path('Personacontacto/editar/<int:pk>', PersonacontactoActualizar.as_view(template_name = "Personacontacto/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Personacontacto o registro de la Base de Datos 
    path('Personacontacto/eliminar/<int:pk>', PersonacontactoEliminar.as_view(), name='Personacontacto/eliminar.html'),




# La ruta 'detalles' en donde mostraremos una página con los detalles de un Sintomas o registro 
    path('Sintomas/detalle/<int:pk>', SintomasDetalle.as_view(template_name = "Sintomas/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Sintomas o registro  
    path('Sintomas/crear', SintomasCrear.as_view(template_name = "Sintomas/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Sintomaso registro de la Base de Datos 
    path('Sintomas/editar/<int:pk>', SintomasActualizar.as_view(template_name = "Sintomas/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Sintomas o registro de la Base de Datos 
    path('Sintomas/eliminar/<int:pk>', SintomasEliminar.as_view(), name='Sintomas/eliminar.html'),



 # La ruta 'detalles' en donde mostraremos una página con los detalles de un Tipopersona o registro 
    path('Tipopersona/detalle/<int:pk>', TipopersonaDetalle.as_view(template_name = "Tipopersona/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Tipopersona o registro  
    path('Tipopersona/crear', TipopersonaCrear.as_view(template_name = "Tipopersona/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Tipopersonao registro de la Base de Datos 
    path('Tipopersona/editar/<int:pk>', TipopersonaActualizar.as_view(template_name = "Tipopersona/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Tipopersona o registro de la Base de Datos 
    path('Tipopersona/eliminar/<int:pk>', TipopersonaEliminar.as_view(), name='Tipopersona/eliminar.html'),




# La ruta 'detalles' en donde mostraremos una página con los detalles de un Tiposangre o registro 
    path('Tiposangre/detalle/<int:pk>', TiposangreDetalle.as_view(template_name = "Tiposangre/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Tiposangre o registro  
    path('Tiposangre/crear', TiposangreCrear.as_view(template_name = "Tiposangre/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Tiposangreo registro de la Base de Datos 
    path('Tiposangre/editar/<int:pk>', TiposangreActualizar.as_view(template_name = "Tiposangre/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Tiposangre o registro de la Base de Datos 
    path('Tiposangre/eliminar/<int:pk>', TiposangreEliminar.as_view(), name='Tiposangre/eliminar.html'),



 # La ruta 'detalles' en donde mostraremos una página con los detalles de un Tiposervicio o registro 
    path('Tiposervicio/detalle/<int:pk>', TiposervicioDetalle.as_view(template_name = "Tiposervicio/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Tiposervicio o registro  
    path('Tiposervicio/crear', TiposervicioCrear.as_view(template_name = "Tiposervicio/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Tiposervicioo registro de la Base de Datos 
    path('Tiposervicio/editar/<int:pk>', TiposervicioActualizar.as_view(template_name = "Tiposervicio/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Tiposervicio o registro de la Base de Datos 
    path('Tiposervicio/eliminar/<int:pk>', TiposervicioEliminar.as_view(), name='Tiposervicio/eliminar.html'),

]
   
