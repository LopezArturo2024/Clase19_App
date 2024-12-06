from django.urls import path
from clase19_appch.views import inicio,cursos,profesores,estudiantes,entregables

urlpatterns = [
    path('Portada/', inicio,name="inicio"),
    path('Cursos/', cursos,name="cursos"),
    path('Profesores/', profesores,name="profesores"),
    path('Estudiantes/', estudiantes,name="estudiantes"),
    path('Entregables/', entregables,name="entregables")
]

