from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework import status
from .forms import *
from django.db.models import Prefetch
from rest_framework import generics
from rest_framework.permissions import AllowAny
from oauth2_provider.models import AccessToken

@api_view(['GET'])
def lista_aeropuerto(request):
    aeropuerto = Aeropuerto.objects.prefetch_related(
    Prefetch('aerolinea_de_aeropuerto'),  # ManyToMany con Aerolínea
    Prefetch('vuelos_de_origen'),         # ManyToOne reversa con Vuelo (origen)
    Prefetch('vuelos_de_destino'),        # ManyToOne reversa con Vuelo (destino)
    Prefetch('servicio_aeropuerto')       # ManyToMany con Servicio
)
    serializer = AeropuertoSerializer(aeropuerto, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def lista_aerolinea(request):
    aerolinea = Aerolinea.objects.prefetch_related(
    Prefetch('aeropuerto'),               # ManyToMany con Aeropuerto
    Prefetch('vuelo_aerolinea')           # ManyToMany con Vuelo
)
    serializer = AerolineaSerializer(aerolinea, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def lista_vuelo(request):
    vuelo = Vuelo.objects.prefetch_related(
    Prefetch('vuelo_pasajero'),           # ManyToMany con Pasajero
    Prefetch('asiento_vuelo'),            # ManyToOne con Asiento
    Prefetch('vuelo_media_aerolinea'),    # ManyToOne con VueloAerolinea
    Prefetch('vuelo_datos')               # OneToOne con EstadisticasVuelo
).select_related(
    'origen',                             # ManyToOne con Aeropuerto (origen)
    'destino'                             # ManyToOne con Aeropuerto (destino)
)
    #serializer = LibroSerializer(libros, many=True)
    serializer = VueloSerializer(vuelo, many=True)
    return Response(serializer.data)


