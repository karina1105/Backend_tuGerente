from rest_framework import serializers
from reserva.models import (
    Cliente,
    Estado_Habitacion,
    Estado_Reserva,
    Habitacion,
    Metodo_Pago,
    Reserva, 
    Factura,
    Factura_Detalle
    )

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class Estado_HabitacionSerializer(serializers.ModelSerializer):
   class Meta:
      model = Estado_Habitacion
      fields = '__all__'

class HabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        fields = '__all__'

class HabitacionIdSerializer(serializers.ModelSerializer):
  id_estado_habitacion = Estado_HabitacionSerializer(read_only=True)
  class Meta:
    model = Habitacion
    fields = '__all__'

class Estado_ReservaSerializer(serializers.ModelSerializer):
   class Meta:
      model = Estado_Reserva
      fields = '__all__'

class Metodo_PagoSerializer(serializers.ModelSerializer):
   class Meta:
      model = Metodo_Pago
      fields = '__all__'


class ReservaSerializer(serializers.ModelSerializer):
   class Meta:
      model = Reserva
      fields = '__all__'

class ReservaIdSerializer(serializers.ModelSerializer):
   id_cliente = ClienteSerializer(read_only=True)
   id_habitacion = HabitacionSerializer(read_only=True)
   id_estado_reserva = Estado_ReservaSerializer(read_only=True)
   class Meta:
      model = Reserva
      fields = '__all__'

class FacturaSerializer(serializers.ModelSerializer):
   class Meta:
      model = Factura
      fields = '__all__'

class FacturaIdSerializer(serializers.ModelSerializer):
   id_cliente = ClienteSerializer(read_only=True)
   class Meta:
      model = Factura
      fields = '__all__'

class FacturaReservaSerializer(serializers.ModelSerializer):
   class Meta:
      model = Factura_Detalle
      fields = '__all__'

class FacturaReservaIdSerializer(serializers.ModelSerializer):
   id_factura = FacturaSerializer(read_only=True)
   id_reserva = ReservaSerializer(read_only=True)
   class Meta:
      model = Factura_Detalle
      fields = '__all__'