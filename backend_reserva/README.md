# backend_Reserva_habitacion_hotel

Maria Karina Limachi Yujra


License: MIT

### JUSTIFICACION ENDPOINTS
La documentanción detallada de la base de datos, flujo de la reserva y los endpoints se encuentran en el archivo /backend_reserva/

resumen de los endpoints:

# Obtiene la Lista de todos los clientes Registrados
api/v1/lista_clientes/ [name='Lista Clientes']

# La Api es necesaria para registrar un cliente nuevo, que desee realizar la reserva de una habitacion
api/v1/registrar_cliente/

# La api obtiene el  registro de un cliente segun su numero de Identificacion
api/v1/buscar_cliente/<str:id>/

# La api realiza la actualizacion del registro de un cliente
api/v1/editar_cliente/<int:id>/ 

# Permite eliminar el registro de una cliente a travez de la llave principal del registro
api/v1/eliminar_cliente/<int:id>/ 

# Sector Estados Habitacion, para no repetir registros sobre el estado de una habitaciones (Disponible, mantenimiento, refacciones)
#Registra el estado en el que podria encontrarse una habitacion
api/v1/registra_estado_habitacion/

# Devuelve la lista de estados registrados
api/v1/lista_estado_habitacion/ 

# Devuelve la lista de habitaciones registradas en la BD 
api/v1/lista_habitaciones/ 

#Devuelve el registro de una habitacion segun su Id_habitacion
api/v1/habitacion/<int:id>/ 

# Permite registrar una nueva habitacion
api/v1/registrar_habitacion/ 

# Permite editar el registro de una habitacion, cambiar estado, agregar una descripcion
api/v1/editar_habitacion/<int:id>/ 

#SeccionEstado Reseva, se creo para crear una indexacion a con el estado de la reserva(Pendiente, pagada, Eliminada), y no registrar el texto como tal
# Resitra los posibles estados en el que se podria encontrar una reservacion
api/v1/registra_estado_reserva/ 

# devuevle la lista de estados registrados, en el que podria estar una reserva
api/v1/lista_estados_reserva/ 

# devuelve la lista de reservas registradas en la BD
api/v1/lista_reservas/ 

# Devuelve el registro(detalle) de una reserva, segun su id_reserva
api/v1/busca_reserva/<int:id>/ 

# Permite registrar una nueva reserva
api/v1/registra_reserva/

# permite editar datos de una reserva
api/v1/editar_reserva/<int:id>/ 

# permite registrar los metodos de pago que seran admitidos por la entidad
api/v1/registra_metodos_pago/ 

# Devuelve la lista de metodos de pago admintidos
api/v1/lista_metodos_pago/ 

# Lista todas las facturas registradas 
api/v1/lista_facturas/ 

# permite registrar una nueva Factrua
api/v1/registrar_factura/ 

# Permite buscar el registro de una Factura, segun su id_factura
api/v1/buscar_factura/<int:id>/ 

#Registra la relacion de la factura con la o las reservas pagadas
api/v1/registrar_detalle_factura/ 

#Permite eliminar la relacion de una factura con una reserva
api/v1/eliminar_detalle_reserva/<int:idf>/<int:idr>/

#permimte buscar las reservas que estan relacionadas con una factura, segun su id_factura
api/v1/buscar_detalle_factura/<int:id>/

#Permite buscar la factura en que fue registrado el pago de una reserva segun su id_reserva
api/v1/buscar_reserva_factura/<int:id>/