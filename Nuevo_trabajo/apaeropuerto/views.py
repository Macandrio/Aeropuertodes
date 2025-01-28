from django.shortcuts import render
import requests
from django.core import serializers



def index(request):
    return render(request, 'index.html')

BASE_API_URL = "http://127.0.0.1:8000/api/v1/"

def aeropuerto_listar_api(request):
    headers = {'Authorization': 'Bearer K7pmCsYBT0EPNIT3N8OdkLYOBR7rhj'}
    response = requests.get(BASE_API_URL + 'Aeropuerto', headers=headers)

    aeropuertos = response.json()
    return render(request, 'paginas/aeropuerto_list.html', {"aeropuertos":aeropuertos})


def aerolinea_listar_api(request):
    response = requests.get(BASE_API_URL + 'Aerolinea')
    aerolineas = response.json()
    return render(request, 'paginas/aerolinea_list.html', {'aerolineas': aerolineas})

def vuelo_listar_api(request):
    response = requests.get(BASE_API_URL + 'Vuelo')
    vuelos = response.json()
    return render(request, 'paginas/vuelo_list.html', {'vuelos': vuelos})
