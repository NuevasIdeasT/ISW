from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

def index(request):
    """View que muestra la pagina principal"""
    return render(request, 'cliente/index.html', {})
    """render(request,template_name,context) en este caso como es el index el 
    contexto esta vacio porque no necesitamos nada."""


def Membresias(request):
    """View que muestra la pagina de membresias"""
    return render(request, 'cliente/Membresia.html', {})

def Login(request):
    """View que muestra el login"""
    return render(request, 'cliente/login.html', {})
 
def Inicio(request):
    """View que muestra la pagina de cursos"""
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    print user
    if user is not None:
        # Correct password, and the user is marked "active"
        login(request, user)
        user = User.objects.get(username=user)
        # Redirect to a success page.
        return render(request, 'cliente/inicioCliente.html', {'user':user,'full_name':user.get_full_name()})
    else:
        # Show an error page
        return HttpResponseRedirect("/login")
    #return render(request, 'cliente/login.html', {})

def Cursos(request):
    """View que muestra la pagina de cursos"""
    return render(request, 'cliente/cursos.html', {})

