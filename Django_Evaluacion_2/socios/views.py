from django.shortcuts import render, redirect
from socios.forms import FormSocio

from socios.models import Socio

# Create your views here.

def index(request):
    return render(request, 'index.html')

def listadoSocios(request):
    socios = Socio.objects.all()
    data = {'socios': socios}
    return render(request, 'socio.html', data)

def agregarSocio(request):
    form = FormSocio()
    if request.method == 'POST':
        form = FormSocio(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregar_socio.html', data)

def eliminarSocio(request, id):
    pro = Socio.objects.get(id = id)
    pro.delete()
    return redirect('/socio/')

def actualizarSocio(request, id):
    pro = Socio.objects.get(id = id)
    form = FormSocio(instance=pro)
    if request.method == 'POST':
        form = FormSocio(request.POST, instance=pro)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregar_socio.html', data)
