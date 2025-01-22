from django.urls import path

from  .api_views import *

urlpatterns = [
    path('Aeropuerto',lista_aeropuerto),
    path('Aerolinea',lista_aerolinea),
    path('Vuelo',lista_vuelo),
]