from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request,"clase19_appch/index.html")

