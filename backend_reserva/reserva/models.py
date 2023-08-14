from django.db import models
from django.utils import timezone

# Create your models here.

class Cliente(models.Model):
  id_cliente = models.AutoField(primary_key=True,verbose_name="Id Cliente")
  nombres = models.CharField(verbose_name="Nombres",max_length= 50)
  primer_apellido = models.CharField(verbose_name="Primer Apellido",max_length = 25)
  segundo_apellido = models.CharField(verbose_name="Segundo Apellido",max_length =25, blank=True)
  numero_ide = models.CharField(verbose_name="Numero Identificación",max_length = 15)
  direccion = models.CharField(verbose_name="Dirección",max_length = 100)
  telefono = models.IntegerField(verbose_name="Teléfono",null = True, blank=True)
  celular = models.IntegerField(verbose_name="Celular",null = False)
  nit = models.IntegerField(verbose_name="Nit", null=False, blank=True)
  def __int__(self):
    return self.id_cliente
  class Meta:
    verbose_name_plural = ("Cliente")

class Estado_Habitacion(models.Model):
  id_estado_habitacion = models.AutoField(primary_key=True, verbose_name="id estado habitacion")
  descripcion = models.CharField(verbose_name="Descripcion",max_length = 100)
  def __int__(self):
    return self.id_estado_habitacion
  class Meta:
    verbose_name_plural = ("Estado_Habitacion")

class Habitacion(models.Model):
  id_habitacion = models.AutoField(primary_key=True,verbose_name="Id Habitacion")
  id_estado_habitacion = models.ForeignKey(Estado_Habitacion, on_delete=models.CASCADE, verbose_name="id estado habitacion")
  nro = models.IntegerField(verbose_name="Numero Habitacion",null=False)
  ubicacionpiso = models.IntegerField(verbose_name="Piso/Planta")
  tipo = models.CharField(verbose_name="Tipo de Habitacion",max_length = 30)
  nro_camas = models.IntegerField(verbose_name="Numero de camas")
  precio_noche = models.DecimalField(verbose_name="Precio Noche", max_digits=5, decimal_places=2, default='100')
  descripcion = models.CharField(verbose_name="Detalle/Observacion",max_length = 150)
  def __int__(self):
    return self.id_habitacion
  class Meta:
    verbose_name_plural = ("Habitacion")



class Estado_Reserva(models.Model):
  id_estado_reserva = models.AutoField(primary_key=True, verbose_name="Id Estado Reserva")
  descripcion = models.CharField(verbose_name="Descripcion",max_length = 100)
  def __int__(self):
    return self.id_estado_reserva
  class Meta:
    verbose_name_plural = ("Estado_Reserva")

class Metodo_Pago(models.Model):
  id_metodo_pago = models.AutoField(primary_key=True, verbose_name="Id_metodo_pago")
  descripcion = models.CharField(verbose_name="Descripcion Metodo Pago",max_length = 50)

  def __int__(self):
    return self.id_metodo_pago
  class Meta:
    verbose_name_plural = ("Metodo_Pago")

class Factura(models.Model):
  id_factura = models.AutoField(primary_key=True, verbose_name="Id Factura")
  id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente")
  fecha_hora = models.DateTimeField(verbose_name="Fecha Hora", default = timezone.now)
  monto_total = models.DecimalField(verbose_name="Monto Total", max_digits=5, decimal_places=2)

  def __int__(self):
    return self.id_factura
  class Meta:
    verbose_name_plural = ("Factura")

class Reserva(models.Model):
  id_reserva = models.AutoField(primary_key=True, verbose_name="Codigo Reserva")
  id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente")
  id_habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE, verbose_name="Habitacion")
  id_estado_reserva = models.ForeignKey(Estado_Reserva, on_delete=models.CASCADE, verbose_name="Estado Reserva")
  fecha_ingreso = models.DateField(verbose_name="Fecha Ingreso")
  fecha_salida = models.DateField(verbose_name="Fecha Salida")
  costo_total = models.DecimalField(verbose_name="Costo total", max_digits=5, decimal_places=2)
  fecha_hora_registro = models.DateTimeField(verbose_name="Fecha Hora Registro", default = timezone.now)
  fecha_hora_editar = models.DateTimeField(verbose_name="Fecha Hora Edicion", default = timezone.now)

  def __int__(self):
    return self.id_factura
  class Meta:
    verbose_name_plural = ("Reserva")

class Factura_Detalle(models.Model):
  id_factura = models.ForeignKey(Factura, on_delete=models.CASCADE, verbose_name="Factura")
  id_reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE, verbose_name="Reserva")
