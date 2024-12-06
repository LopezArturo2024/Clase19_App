from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request,"clase19_appch/index.html")

def cursos(request):
    return render(request,"clase19_appch/cursos.html")

def profesores(request):
    return render(request,"clase19_appch/profesores.html")

def estudiantes(request):
    return render(request,"clase19_appch/estudiantes.html")

def entregables(request):
    return render(request,"clase19_appch/entregables.html")
