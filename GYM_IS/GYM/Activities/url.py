from django.conf.urls import url
from . import views

urlpatterns = [
<<<<<<< HEAD
    url('', views.index, name='actividades'),
=======
    url('index', views.index, name='index'),
    url('formu', views.formulario, name='formu'),
>>>>>>> Luis_Eduardo
]