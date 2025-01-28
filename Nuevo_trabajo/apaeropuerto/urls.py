from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Aeropuerto/', views.aeropuerto_listar_api, name='aeropuerto_listar_api'),
    path('Aerolinea/', views.aerolinea_listar_api, name='aerolinea_listar_api'),
    path('Vuelo/', views.vuelo_listar_api, name='vuelo_listar_api'),

]