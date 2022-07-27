from tkinter import E
from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Estudiante

# Create your views here.
def index(request):
    estudiantes = ['Gomez Marcos Emily',
                   'Pinedo Romero Kevin Arturo'
                   ]
 
    return render(request,'index.html', {
        'titulo':'Inicio',
        'mensaje':'Proyecto Web - UC4 LP3',
        'estudiantes': estudiantes
    })

def saludo(request):
    return render(request,'saludo.html',{
         'titulo': 'Saludo',
         'autor_saludo':'Les damos un saludo al sitio web de Emily y Kevin'
    })
       
def crear_estudiante(request, codigo, dni, nombre, apepat, apemat, direccion, estado):
    estudiante = Estudiante(
        codigo = codigo,
        dni = dni,
        nombre = nombre,
        apepat = apepat,
        apemat = apemat,
        direccion = direccion,
        estado =   estado
    )
    estudiante.save()
    return HttpResponse(f"Estudiante Creado: {estudiante.codigo} - {estudiante.dni} - {estudiante.nombre} - {estudiante.apepat} - {estudiante.apemat} - {estudiante.direccion} - {estudiante.estado}")

def buscar_estudiante(request):
    try:
        estudiante = Estudiante.objects.get(id=1000)
        resultado = f"""Articulo: 
                        <br> <strong>ID:</strong> {estudiante.id} 
                        <br> <strong>Codigo:</strong> {estudiante.codigo} 
                        <br> <strong>DNI:</strong> {estudiante.dni}
                        <br> <strong>Nombre:</strong> {estudiante.nombre} 
                        <br> <strong>Apellido Paterno:</strong> {estudiante.apepat}
                        <br> <strong>Apellido Materno:</strong> {estudiante.apemat} 
                        <br> <strong>Dirección:</strong> {estudiante.direccion}
                        <br> <strong>Estado:</strong> {estudiante.estado}
                        """
    except:
        resultado = "<h1> Estudiante No Encontrado, intentalo otra vez </h1>"
    return HttpResponse(resultado)

def editar_estudiante(request, id):
    estudiante = Estudiante.objects.get(pk=id)
 
    estudiante.codigo = 2017110656
    estudiante.dni = 75965737
    estudiante.nombre = "JORDY EUSEBIO"
    estudiante.apepat = "Quispe"
    estudiante.apemat = "Cupe"
    estudiante.direccion = "Villa el Salvador"
    estudiante.estado = False
 
    estudiante.save()
    return HttpResponse(f"Estudiante Editado: {estudiante.codigo} - {estudiante.dni} - {estudiante.nombre} - {estudiante.apepat} - {estudiante.apemat} - {estudiante.direccion} - {estudiante.estado}")

def listar_estudiantes(request):
    estudiantes = Estudiante.objects.all();#estudiante
    """estudiantes = Estudiante.objects.filter(
            Q(nombre__contains="Py") |
            Q(nombre__contains="Hab")
    )"""
    return render(request, 'listar_estudiantes.html',{
        'estudiantes': {estudiantes},
        'nombre': 'Listado de estudiantes'
    })

def eliminar_estudiante(request, id):
    estudiante = Estudiante.objects.get(pk=id)
    estudiante.delete()
    return redirect('listar_estudiantes')

def save_estudiante(request):
    if request.method == 'GET':
        codigo = request.GET['codigo']
        dni = request.GET['dni']
        nombre = request.GET['nombre']
        apepat = request.GET['apepat']
        apemat = request.GET['apemat']
        direccion = request.GET['direccion']
        estado = request.GET['estado']
 
        estudiante = Estudiante(
            codigo = codigo,
            dni = dni,
            nombre = nombre,
            apepat = apepat,
            apemat = apemat,
            direccion = direccion,
            estado =   estado
        )
        estudiante.save()
        return HttpResponse(f"Estudiante Creado: {estudiante.codigo} - {estudiante.dni} - {estudiante.nombre} - {estudiante.apepat} - {estudiante.apemat} - {estudiante.direccion} - {estudiante.estado}")
    else:
        return HttpResponse("<h2>No se ha podido registrar el estudiante</h2>")
 
def create_estudiante(request):
    return render(request, 'create_estudiante.html')