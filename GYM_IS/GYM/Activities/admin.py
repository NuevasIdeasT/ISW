from django.contrib import admin
from .models import Tiposact,Empleados,Ubicacion,Activity
# Register your models here.


admin.site.register(Activity)
admin.site.register(Tiposact)
admin.site.register(Empleados)
admin.site.register(Ubicacion)