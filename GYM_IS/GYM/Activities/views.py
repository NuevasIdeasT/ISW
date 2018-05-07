from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Ubicacion,Tiposact,Empleados
from django.db import connections
from django.db.utils import OperationalError
from django.shortcuts import render


def index(request):
    all_Ubica = Ubicacion.objects.all()
    all_Tipos = Tiposact.objects.all()
    all_Empleados = Empleados.objects.all()
   # all_Actividades = Activity.objects.all()
    context = {
        'all_Ubica': all_Ubica,
        'all_Tipos': all_Tipos,
        'all_Empleados': all_Empleados
       # 'all_Actividades':all_Actividades
               }
    return render(request, 'Actividades.html',context);
