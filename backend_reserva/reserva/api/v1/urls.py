from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    Clientes, BuscaCliente, EditarCliente, EliminarCliente, ListaHabitaciones, DetalleHabitacion, EditarHabitacion,
    EstadosHabitacion, EstadosReserva, MetodosPago, Reservas,BuscarReservas, EditarReserva, Facturas,BuscaFacturas,
    DetalleFactura, BuscaDetalleFactura, BuscaFacturaDetalle, EliminarDetalleFactura
)

app_name = 'reserva'

urlpatterns=[
    ## seccion Clientes
    path('lista_clientes/', Clientes.as_view(), name='Lista Clientes'),
    path('registrar_cliente/', Clientes.as_view(), name='Registra Cliente Nuevo'),
    path('buscar_cliente/<str:id>/', BuscaCliente.as_view(), name='Buscar Cliente con Identificacion X'),
    path('editar_cliente/<int:id>/', EditarCliente.as_view(), name="Editar Cliente"),
    path('eliminar_cliente/<int:id>/', EliminarCliente.as_view(), name="Eliminar Registro Cliente"),

    ## seccion Habitaciones EstadoHabitaciones('Disponible', 'Remodelacion', 'Refaccion')
    path('registra_estado_habitacion/', EstadosHabitacion.as_view(), name = "registra estados para las habitaciones"),
    path('lista_estado_habitacion/', EstadosHabitacion.as_view(), name = "Lista de estados para las habitaciones"),
    path('lista_habitaciones/', ListaHabitaciones.as_view(), name='Lista Habitaciones'),
    path('habitacion/<int:id>/', DetalleHabitacion.as_view(), name='Busca Habitacion con id X'),
    path('registrar_habitacion/', ListaHabitaciones.as_view(), name='Registrar Nueva Habitacion'),
    path('editar_habitacion/<int:id>/', EditarHabitacion.as_view(), name='Editar Nueva Habitacion'),

    ## seccion Reservaciones  Estado('Pendiente', 'Pagado', 'Eliminado')
    path('registra_estado_reserva/', EstadosReserva.as_view(), name = "registrar estados para reservar"),
    path('lista_estados_reserva/', EstadosReserva.as_view(), name = "Estados de Reservaciones "),

    path('lista_reservas/', Reservas.as_view(), name='Lista de Reservas'),
    path('busca_reserva/<int:id>/', BuscarReservas.as_view(), name='Busca Reserva con Id_reserva'),
    path('registra_reserva/', Reservas.as_view(), name='Registra Nueva Reserva'),
    path('editar_reserva/<int:id>/', EditarReserva.as_view(), name='Edita una Reserva X'),


    ## seccion facturacion  metodos('efectivo', 'tarjeta debito', tarjeta creadito')
    path('registra_metodos_pago/', MetodosPago.as_view(), name='Metodos de Pago'),
    path('lista_metodos_pago/', MetodosPago.as_view(), name='Lista Metodos de Pago'),
    path('lista_facturas/', Facturas.as_view(), name='Lista Facturas'),
    path('registrar_factura/', Facturas.as_view(), name='Registra Factura Nueva'),
    path('buscar_factura/<int:id>/', BuscaFacturas.as_view(), name='Buscar Factura con Id_factura'),

    ## Detalles(reservas) dentro de la factura
    path('registrar_detalle_factura/', DetalleFactura.as_view(), name='Registrar Reservas en detalle de factura X'),
    path('eliminar_detalle_reserva/<int:idf>/<int:idr>/', EliminarDetalleFactura.as_view(), name="Eliminar Registro factura detalle"),
    path('buscar_detalle_factura/<int:id>/', BuscaDetalleFactura.as_view(), name='Buscar detalles de Factura X'),
    path('buscar_reserva_factura/<int:id>/', BuscaFacturaDetalle.as_view(), name='Buscar factura de la reserva con condigo X'),
]