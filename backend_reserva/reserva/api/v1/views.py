from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404 
from django.db.models import Q
from .serializers import (
    ClienteSerializer,
    Estado_HabitacionSerializer,
    Estado_ReservaSerializer,
    HabitacionIdSerializer,
    HabitacionSerializer,
    Metodo_PagoSerializer,
    ReservaSerializer,
    ReservaIdSerializer,
    FacturaSerializer,
    FacturaIdSerializer, 
    FacturaReservaSerializer,
    FacturaReservaIdSerializer
)
from reserva.models import (
    Cliente, Estado_Habitacion, Estado_Reserva, Habitacion, Metodo_Pago, Reserva, Factura, Factura_Detalle

)
# Create your views here.

class Clientes(APIView):
    def get(self, request):
        cliente = Cliente.objects.all()
        serializer= ClienteSerializer(cliente, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ClienteSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        snippet = self.get_object(id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class BuscaCliente(APIView):
    def get(self, request, id, format=None):
       snippets = Cliente.objects.all().filter(numero_ide = id)
       serializer = ClienteSerializer(snippets, many=True)
       return Response(serializer.data)
    
class EditarCliente(APIView):
  def get_object(self, id):
    try:
      return Cliente.objects.get(id_cliente=id)
    except Cliente.DoesNotExist:
      raise Http404
  def get(self, request, id, format=None):
    snippet = self.get_object(id)
    serializer = ClienteSerializer(snippet)
    return Response(serializer.data)
  
  def put(self, request, id, format=None):
    snippet = self.get_object(id)
    serializer = ClienteSerializer(snippet, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request, id, format=None):
    snippet = self.get_object(id)
    snippet.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  
class EliminarCliente(APIView):
  def get_object(self, id):
    try:
      return Cliente.objects.get(id_cliente=id)
    except Cliente.DoesNotExist:
      raise Http404
  def get(self, request, id, format=None):
    snippet = self.get_object(id)
    serializer = ClienteSerializer(snippet)
    return Response(serializer.data)
  
  def delete(self, request, id, format=None):
    snippet = self.get_object(id)
    snippet.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class EstadosHabitacion(APIView):
    def get(self, request):
        estado_h = Estado_Habitacion.objects.all()
        serializer = Estado_HabitacionSerializer(estado_h, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Estado_HabitacionSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EstadosReserva(APIView):
    def get(self, request):
        estado_reserva = Estado_Reserva.objects.all()
        serializer = Estado_ReservaSerializer(estado_reserva, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Estado_ReservaSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListaHabitaciones(APIView):
    def get(self, request):
        habitacion = Habitacion.objects.all()
        serializer = HabitacionSerializer(habitacion, many=True)
        return Response(serializer.data)
        
class DetalleHabitacion(APIView):
    def get(self, request, id, format=None):
       snippets = Habitacion.objects.all().filter(id_habitacion = id)
       serializer = HabitacionIdSerializer(snippets, many=True)
       return Response(serializer.data)
    
    def post(self, request, format = None):
        serializer = HabitacionSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EditarHabitacion(APIView):
  def get_object(self, id):
    try:
      return Habitacion.objects.get(id_habitacion=id)
    except Habitacion.DoesNotExist:
      raise Http404
  def get(self, request, id, format=None):
    snippet = self.get_object(id)
    serializer = HabitacionSerializer(snippet)
    return Response(serializer.data)
  
  def put(self, request, id, format=None):
    snippet = self.get_object(id)
    serializer = HabitacionSerializer(snippet, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request, id, format=None):
    snippet = self.get_object(id)
    snippet.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
   
class MetodosPago(APIView):
    def get(self, request):
        estado_reserva = Metodo_Pago.objects.all()
        serializer = Metodo_PagoSerializer(estado_reserva, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Metodo_PagoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Reservas(APIView):
    def get(self, request):
        estado_reserva = Reserva.objects.all()
        serializer = ReservaSerializer(estado_reserva, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReservaSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BuscarReservas(APIView):
    def get(self, request, id, format=None):
       snippets = Reserva.objects.all().filter(id_reserva = id)
       serializer = ReservaIdSerializer(snippets, many=True)
       return Response(serializer.data)
    
class EditarReserva(APIView):
    def get_object(self, id):
        try:
            return Reserva.objects.get(id_reserva=id)
        except Reserva.DoesNotExist:
            raise Http404
    def get(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = ReservaSerializer(snippet)
        return Response(serializer.data)
    def put(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = ReservaSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BuscaReservaFechas(APIView):
    def get(self, request, fechai, fechaf, format=None):
       snippets = Factura.objects.all().filter(Q(fecha_ingreso__range = (fechai, fechaf)) | Q(fecha_salida__range = (fechai, fechaf)))
       serializer = FacturaIdSerializer(snippets, many=True)
       return Response(serializer.data)

class Facturas(APIView):
    def get(self, request):
        factura = Factura.objects.all()
        serializr= FacturaSerializer(factura, many = True)
        return Response(serializr.data)
    
    def post(self, request):
        serializer = FacturaSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BuscaFacturas(APIView):
    def get(self, request, id, format=None):
       snippets = Factura.objects.all().filter(id_factura = id)
       serializer = FacturaIdSerializer(snippets, many=True)
       return Response(serializer.data)
    
    
class BuscaDetalleFactura(APIView):
    def get(self, request, id, format=None):
       snippets = Factura_Detalle.objects.all().filter(id_factura = id)
       serializer = FacturaReservaIdSerializer(snippets, many=True)
       return Response(serializer.data)
    
class DetalleFactura(APIView):
    def get(self, request):
        factura = Factura.objects.all()
        serializr= FacturaSerializer(factura, many = True)
        return Response(serializr.data)
    
    def post(self, request):
        serializer = FacturaReservaSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BuscaFacturaDetalle(APIView):
   def get(self, request, id, format=None):
       snippets = Factura_Detalle.objects.all().filter(id_reserva=id)
       serializer = FacturaReservaIdSerializer(snippets, many=True)
       return Response(serializer.data)
   
class EliminarDetalleFactura(APIView):
  def get_object(self, idf, idr):
    try:
      return Factura_Detalle.objects.get(id_factura=idf, id_reserva=idr)
    except Factura_Detalle.DoesNotExist:
      raise Http404
  def get(self, request, idf, idr, format=None):
    snippet = self.get_object(idf, idr)
    serializer = FacturaReservaSerializer(snippet)
    return Response(serializer.data)
  
  def delete(self, request, idf, idr, format=None):
    snippet = self.get_object(idf, idr)
    snippet.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)