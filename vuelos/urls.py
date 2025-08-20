from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("vuelos/registrar/", views.registrar_vuelo, name="registrar_vuelo"),
    path("vuelos/listar/", views.listar_vuelos, name="listar_vuelos"),
    path("vuelos/estadisticas/", views.estadisticas_vuelos, name="estadisticas_vuelos"),
]
