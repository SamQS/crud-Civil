from django.shortcuts import render, redirect
from .models import proyectosCivil
from django.db.models import Q

# Create your views here.


def pryCivil(request):
    busqueda = request.GET.get('buscar')
    proyectoCivil = proyectosCivil.objects.all()

    if busqueda:
        proyectoCivil = proyectosCivil.objects.filter(

            Q(proyecto__icontains = busqueda) |
            Q(direccion__icontains = busqueda) |
            Q(tipoProyecto__icontains = busqueda) |
            Q(projectManager__icontains = busqueda) |
            Q(prioridad__icontains = busqueda) |
            Q(cantidadDias__icontains = busqueda) |
            Q(planosDibus__icontains = busqueda) |
            Q(correciones__icontains = busqueda) |
            Q(obervaciones__icontains = busqueda) 
).distinct()
    return render(request, 'pryCivil.html', {"proyectos": proyectoCivil})

def registrarProyecto(request):
    proyecto = request.POST['txtproyecto']
    direccion = request.POST['txtdireccion']
    tipoProyecto = request.POST['txttipoproyecto']
    projectManager = request.POST['txtprojectmanager']
    prioridad = request.POST['txtprioridad']
    nuevoProyecto = request.POST['txtnuevoproyecto']
    propuesta = request.POST['txtpropuesta']
    cantidadDias = request.POST['txtdias']
    envioPropCliente = request.POST['txtenvioPropuesta']
    clienteAprobado = request.POST['txtclienteAprobado']
    proyectoExistente = request.POST['txtproyectoExistente']
    tipoServicio = request.POST['txttipoServicio']
    planosCadCliente = request.POST['txtplanosCliente']
    planosDibus = request.POST['txtplanosdibus']
    correciones = request.POST['txtcorrecciones']
    obervaciones = request.POST['txtobservaciones']
    fechaEntrega = request.POST['txtfecha']
    pc = request.POST['txtpc']
    

    registroProy = proyectosCivil.objects.create(
    proyecto=proyecto,
    direccion = direccion,
    tipoProyecto = tipoProyecto,
    projectManager = projectManager,
    prioridad = prioridad,
    nuevoProyecto = nuevoProyecto,
    propuesta = propuesta,
    cantidadDias = cantidadDias,
    envioPropCliente = envioPropCliente,
    clienteAprobado = clienteAprobado,
    proyectoExistente = proyectoExistente,
    tipoServicio = tipoServicio,
    planosCadCliente = planosCadCliente,
    planosDibus = planosDibus,
    correciones = correciones,
    obervaciones = obervaciones,
    fechaEntrega = fechaEntrega,
    pc = pc)
    return redirect('/')


def edicionProyecto(request, codigo):
    registroProy = proyectosCivil.objects.get(codigo=codigo)
    return render(request,  "edicionProyecto.html", {"registroProy":registroProy})

def editarProyecto(request):
    codigo = request.POST['txtcod']
    proyecto = request.POST['txtproyecto']
    direccion = request.POST['txtdireccion']
    tipoProyecto = request.POST['txttipoproyecto']
    projectManager = request.POST['txtprojectmanager']
    prioridad = request.POST['txtprioridad']
    nuevoProyecto = request.POST['txtnuevoproyecto']
    propuesta = request.POST['txtpropuesta']
    cantidadDias = request.POST['txtdias']
    envioPropCliente = request.POST['txtenvioPropuesta']
    clienteAprobado = request.POST['txtclienteAprobado']
    proyectoExistente = request.POST['txtproyectoExistente']
    tipoServicio = request.POST['txttipoServicio']
    planosCadCliente = request.POST['txtplanosCliente']
    planosDibus = request.POST['txtplanosdibus']
    correciones = request.POST['txtcorrecciones']
    obervaciones = request.POST['txtobservaciones']
    fechaEntrega = request.POST['txtfecha']
    pc = request.POST['txtpc']

    registroProy = proyectosCivil.objects.get(codigo=codigo)
    registroProy.proyecto = proyecto
    registroProy.direccion = direccion
    registroProy.tipoProyecto = tipoProyecto
    registroProy.projectManager = projectManager
    registroProy.prioridad = prioridad
    registroProy.nuevoProyecto = nuevoProyecto
    registroProy.propuesta = propuesta
    registroProy.cantidadDias = cantidadDias
    registroProy.envioPropCliente = envioPropCliente
    registroProy.clienteAprobado = clienteAprobado
    registroProy.proyectoExistente = proyectoExistente
    registroProy.tipoServicio = tipoServicio
    registroProy.planosCadCliente = planosCadCliente
    registroProy.planosDibus = planosDibus
    registroProy.correciones = correciones
    registroProy.obervaciones = obervaciones
    registroProy.fechaEntrega = fechaEntrega
    registroProy.pc = pc
    registroProy.save()

    return redirect('/')

def eliminarProyecto(request, codigo):

    registroProy = proyectosCivil.objects.get(codigo=codigo)
    registroProy.delete()

    return redirect('/')

def archivarProyecto(request, codigo):
    registroProy = proyectosCivil.objects.get(codigo=codigo)
    registroProy.archivado = True

