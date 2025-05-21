from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('lista_peliculas/',views.vista_peliculas, name='lista_peliculas'),
    path('agregar_pelicula/',views.vista_agregar_pelicula, name = 'vista_agregar_pelicula'),
    path('agregar_genero/',views.vista_agregar_genero, name = 'vista_agregar_genero'),
]
