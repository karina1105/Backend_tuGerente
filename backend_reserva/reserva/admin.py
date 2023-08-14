from django.contrib import admin

# Register your models here.
from .models import (
    Cliente, Estado_Habitacion, Habitacion, Estado_Reserva, Metodo_Pago, Factura, Reserva, Factura_Detalle
)

admin.site.register(Cliente)

admin.site.register(Estado_Habitacion)

admin.site.register(Habitacion)

admin.site.register(Estado_Reserva)

admin.site.register(Metodo_Pago)

admin.site.register(Factura)

admin.site.register(Reserva)

admin.site.register(Factura_Detalle)