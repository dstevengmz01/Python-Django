from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import render,redirect


def inicio(request):
    return render(request,'inicio.html')

def vista_agregar_pelicula(request):
    if request.method == 'POST':
        formulario = agregar_pelicula_form(request.POST, request.FILES)
        if formulario.is_valid():
            peli = formulario.save(commit = False)
            peli.status = True
            peli.save()
            formulario.save_m2m()
            return redirect ('/inicio')
    else:
        formulario = agregar_pelicula_form()
    return render(request, 'vista_agregar_pelicula.html', locals())


def vista_agregar_genero(request):
    if request.method == 'POST':
        formulario = agregar_genero_form(request.POST, request.FILES)
        if formulario.is_valid():
            peli = formulario.save(commit = False)
            peli.status = True
            peli.save()
            formulario.save_m2m()
            return redirect ('/inicio/')
    else:
            formulario = agregar_genero_form()
    return render(request, 'vista_agregar_genero.html', locals()) 