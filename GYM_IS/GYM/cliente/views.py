from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
	
def index(request):
	"""View que muestra la pagina principal"""
	
	return render(request, 'cliente/index.html',{})
	#render(request,template_name,context) en este caso como es el index el contexto esta vacio porque no necesitamos nada.
def Membresias(request):
	"""View que muestra la pagina de membresias"""
	return render(request,'cliente/Membresia.html',{})
def Login(request):
	"""View que muestra la pagina de membresias"""
	return render(request,'cliente/login.html',{})