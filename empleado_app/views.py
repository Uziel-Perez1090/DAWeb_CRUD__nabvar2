from django.shortcuts import render,redirect
from.models import Empleado
# Create your views here.

def inicio_vistaEmpleado(request):
    losnegocios=Empleado.objects.all()

    return render(request,"gestionarNegocio.html",{"misnegocios":losnegocios})


def registrarEmpleado(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["txttelefono"]
    email=request.POST["txtemail"]
    apellido=request.POST["txtapellido"]
    id_sucursal=request.POST["txtid_sucursal"]
    guardarempleado=Empleado.objects.create(codigo=codigo,nombre=nombre,direccion=direccion,telefono=telefono,email=email,apellido=apellido,id_sucursal=id_sucursal)
    return redirect("Empleado")

def seleccionarEmpleado(request,codigo):
    negocio=Empleado.objects.get(codigo=codigo)
    return render(request,"editarNegocio.html",{"misnegocios":negocio})

def editarEmpleado(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["txttelefono"]
    email=request.POST["txtemail"]
    apellido=request.POST["txtapellido"]
    id_sucursal=request.POST["txtid_sucursal"]
    negocio=Empleado.objects.get(codigo=codigo)
    negocio.nombre=nombre
    negocio.direccion=direccion
    negocio.telefono=telefono
    negocio.email=email
    negocio.apellido=apellido
    negocio.id_sucursal=id_sucursal
    negocio.save()
    return redirect("Empleado")

def borrarEmpleado(request,codigo):
    materia=Empleado.objects.get(codigo=codigo)
    materia.delete()
    return redirect("Empleado")