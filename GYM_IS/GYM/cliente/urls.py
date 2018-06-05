from django.conf.urls import include, url
from . import views

app_name = 'cliente'
urlpatterns = [
    url(
        regex=r'^$',
        view=views.index,
        name='index'
    ),
    url(
        regex=r'^membresias/$',
        view=views.Membresias,
        name='membresias'
    ),
    url(
        regex=r'^login/$',
        view=views.Login,
        name='login'
    ),
    url(
        regex=r'^cursos/$',
        view=views.Cursos,
        name='cursos'
    ),
    url(
        regex=r'^inicio/$',
        view=views.Inicio,
        name='inicioCliente'
    ),
]
