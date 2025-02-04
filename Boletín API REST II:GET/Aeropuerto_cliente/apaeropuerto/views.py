from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from .helper import helper
import json
from requests.exceptions import HTTPError

import requests
import environ
import os
from pathlib import Path


# Cargar variables de entorno
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'), True)
env = environ.Env()

BASE_API_URL = "https://macandrio.pythonanywhere.com/api/v1/"

def index(request):
    return render(request, 'index.html')

#------------------------------------------------Listar--------------------------------------------------------------
def aeropuerto_listar_api(request):
    if (request.user.is_anonymous==False):     
        if (request.user and request.user.rol == 1):       
            headers = {'Authorization': 'Bearer '+env('Admin')} 
        elif (request.user and request.user.rol == 2):
            headers = {'Authorization': 'Bearer '+env('PASAJERO')} 
        else:
            headers = {'Authorization': 'Bearer '+env('GERENTE')}
    else:
        headers = {'Authorization': 'Bearer '+env('PASAJERO')}


    response = requests.get(BASE_API_URL + 'Aeropuerto', headers=headers)
    aeropuertos = response.json()
    return render(request, 'paginas/aeropuerto_list.html', {"aeropuertos": aeropuertos})

def aerolinea_listar_api(request):
    if (request.user.is_anonymous==False):     
        if (request.user and request.user.rol == 1):       
            headers = {'Authorization': 'Bearer '+env('Admin')} 
        elif (request.user and request.user.rol == 2):
            headers = {'Authorization': 'Bearer '+env('PASAJERO')} 
        else:
            headers = {'Authorization': 'Bearer '+env('GERENTE')}
    else:
        headers = {'Authorization': 'Bearer '+env('PASAJERO')}
    response = requests.get(BASE_API_URL + 'Aerolinea', headers=headers)
    aerolineas = response.json()
    return render(request, 'paginas/aerolinea_list.html', {'aerolineas': aerolineas})


def vuelo_listar_api(request):
    if (request.user.is_anonymous==False):     
        if (request.user and request.user.rol == 1):       
            headers = {'Authorization': 'Bearer '+env('Admin')} 
        elif (request.user and request.user.rol == 2):
            headers = {'Authorization': 'Bearer '+env('PASAJERO')} 
        else:
            headers = {'Authorization': 'Bearer '+env('GERENTE')}
    else:
        headers = {'Authorization': 'Bearer '+env('PASAJERO')}
    response = requests.get(BASE_API_URL + 'Vuelo', headers=headers)
    vuelos = response.json()
    return render(request, 'paginas/vuelo_list.html', {'vuelos': vuelos})

def reserva_listar_api(request):
    if (request.user.is_anonymous==False):     
        if (request.user and request.user.rol == 1):       
            headers = {'Authorization': 'Bearer '+env('Admin')} 
        elif (request.user and request.user.rol == 2):
            headers = {'Authorization': 'Bearer '+env('PASAJERO')} 
        else:
            headers = {'Authorization': 'Bearer '+env('GERENTE')}
    else:
        headers = {'Authorization': 'Bearer '+env('PASAJERO')}
    response = requests.get(BASE_API_URL + 'Reserva', headers=headers)
    reservas = response.json()
    return render(request, 'paginas/reserva_list.html', {'reservas': reservas})


def vueloaerolinea_listar_api(request):
    if (request.user.is_anonymous==False):     
        if (request.user and request.user.rol == 1):       
            headers = {'Authorization': 'Bearer '+env('Admin')} 
        elif (request.user and request.user.rol == 2):
            headers = {'Authorization': 'Bearer '+env('PASAJERO')} 
        else:
            headers = {'Authorization': 'Bearer '+env('GERENTE')}
    else:
        headers = {'Authorization': 'Bearer '+env('PASAJERO')}
    response = requests.get(BASE_API_URL + 'Vueloaerolinea', headers=headers)
    vueloaerolinea = response.json()
    return render(request, 'paginas/vuelo_aerolinea_list.html', {'vueloaerolinea': vueloaerolinea})


#------------------------------------------------Formularios------------------------------------------------------------
def crear_cabecera():
    return {
        'Authorization': 'Bearer '+env("TOKEN_ACCESO"),
        "Content-Type": "application/json"
        }


def Aeropuerto_busqueda_simple(request):
    formulario = BusquedaAeropuertoForm(request.GET)
    
    if formulario.is_valid():
        headers = crear_cabecera()
        response = requests.get(
            BASE_API_URL + 'Aeropuerto/busqueda_simple',
            headers=headers,
            params={'textoBusqueda':formulario.data.get("textoBusqueda")}
        )
        aeropuerto = response.json()
        return render(request, 'Formularios/Aeropuerto/busqueda_avanzada.html',{"aeropuerto_mostrar":aeropuerto})
    if("HTTP_REFERER" in request.META):
        return redirect(request.META["HTTP_REFERER"])
    else:
        return redirect("index")
