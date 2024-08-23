from django.shortcuts import render, redirect
from .models import Tareas
from .form import TareasForm

# Create your views here.

def crear(request):
    if request.method == 'POST':
        form = TareasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar')
    form = TareasForm()
    return render(request,'crear.html',{'form':form})

def listar(request):
    tareas = Tareas.objects.all()
    return render(request,'listar.html',{'tareas':tareas})