from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Ubicacion,Tiposact,Empleados,Activity
from django.db import connections
from django.db.utils import OperationalError
from django.shortcuts import render
from django.core import serializers
from django.forms import Form
from .forms import Homeform
from django.views.generic import TemplateView

# assuming obj is a model instance


def index(request):
    all_Ubica = Ubicacion.objects.all()
    all_Tipos = Tiposact.objects.all()
    all_Empleados = Empleados.objects.all()
    all_Actividades = Activity.objects.all()
    context = {
        'all_Ubica': all_Ubica,
        'all_Tipos': all_Tipos,
        'all_Empleados': all_Empleados,
        'all_Actividades':all_Actividades
               }


    return render(request, 'Actividades.html',context);

class formulario(TemplateView):
    def post(self,request):
        if request.method == 'POST':
            form = Homeform(request.POST)
            if form.is_valid():
                print('Es Valido')
                text = form.cleaned_datax
        return render(request,'FormExample.html',{'form': form});