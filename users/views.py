from django.shortcuts import render, redirect
from .models import Persona
from .form import PersonaForm
# Create your views here.

def listar_personas(request):
    personas = Persona.objects.all()
    return render(request,'listar_personas.html',{'personas':personas})

def crear_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect(listar_personas)
    else:
        form = PersonaForm()
        return render(request,'crear_persona.html',{'form':form})
        
