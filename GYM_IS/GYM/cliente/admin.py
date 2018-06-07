from django.contrib import admin

from .models import (
    Cliente,
    Sucursal,
    Membresia
)

admin.site.register(Cliente)
admin.site.register(Sucursal)
admin.site.register(Membresia)

# Register your models here.
