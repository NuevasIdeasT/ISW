from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator

# Create your models here.

User = get_user_model()
"""La funcion get_user_model sirve para obtener el modelo que se este usando actualmente en la aplicacion.
El otro import es una utilidad de Django para validar los atributos de nuestros modelos en disntintos 
parametro (longitud,tipo,etc.)"""


class Cliente(models.Model):
    """Modelo de cliente aqui definimos los atributos y relaciones que tendra nuestros clientes."""

    nombre_de_usuario = models.CharField('Nombre de usuario', max_length=20,unique=True,null=True)
    contrasenia = models.CharField('Contrasenia del cliente', max_length=16,null=True)
    nombre = models.CharField('Nombre del cliente', max_length=50)
    domicilio = models.TextField('direccion del cliente')
    correo = models.CharField('Correo', max_length=30)
    telefono = models.CharField('Telefono', max_length=10)
    numero_emergencia = models.CharField(
        'Numero de emergencia', max_length=10, blank=True)
    fecha_nacimiento = models.DateField('Fecha de nacimiento')
    estatura = models.FloatField('Estatura')
    peso = models.FloatField('Peso')
    alergias = models.IntegerField('Alergias', blank=True)
    enfermedades_cronicas = models.IntegerField(
        'Enfermedades cronicas', blank=True)
    medicamentos = models.IntegerField('Nombre del cliente', blank=True)
    ID_sucursal = models.ForeignKey('cliente.Sucursal')
    ID_membresia = models.ForeignKey('cliente.Membresia')

    """Metodo para definir como se muestra un objeto instanciado de esta clase algo como un toString."""
    """Cliente.objects.create(nombre="Gabriel", domicilio="Villa de aragon no. 199 col. valle de aragon
     CdMx", correo="gabo_2@hotmail.com", telefono="5543785629", fecha_nacimiento=fechaN, estatura=1.70,
      peso=68.0,alergias=0, enfermedades_cronicas=0, medicamentos=0,  
      ID_sucursal=Sucursal.objects.get(pk=1), ID_membresia=Membresia.objects.get(pk=1))"""

    def __str__(self):
        return "'{nombre} y {correo}".format(
            nombre=self.nombre,
            correo=self.correo
        )


class Membresia(models.Model):
    """MOdelo de Membresia definimos sus atributos """

    tipo = models.IntegerField('Tipo de membresia')
    nombre = models.CharField('Nombre de membresia',
                              max_length=12, unique=True)
    descripcion = models.TextField('Descripcion')
    costo = models.IntegerField('Costo')

    """Metodo para definir como se muestra un objeto instanciado de esta clase algo como un toString."""

    def __str__(self):
        return self.nombre


class Sucursal(models.Model):
    """Modelo de sucursal donde definimos sus atributos y relaciones"""
    nombre = models.CharField('Nombre de la sucursal',
                              max_length=20, unique=True)
    direccion = models.TextField('Direccion donde se ubica.')
    telefono = models.CharField('Telefono', max_length=10)
    hora_apertura = models.TimeField('Hora de apertura')
    hora_cierre = models.TimeField('Hora de cierre')

    def __str__(self):
        return self.nombre
