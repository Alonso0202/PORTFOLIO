from django.shortcuts import render
from .models import Project
# Create your views here.

'''Creamos la funcion para acceder a nuestra carpeta template'''
def home(request):
    projects=Project.objects.all()
    return render(request, 'home.html',{'projects': projects})
