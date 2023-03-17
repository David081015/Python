from django.shortcuts import render, redirect, get_object_or_404
from personas.models import Persona
from personas.forms import Personaform
# Create your views here.
def nuevaPersona(request):
    if request.method == 'POST':
        formaPersona = Personaform(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('indexPersonas')
    else:
        formaPersona = Personaform()
    return render(request,'nuevo.html',{'formaPersona':formaPersona})

def editarPersona(request,id):
    persona = get_object_or_404(Persona,pk=id)
    if request.method == 'POST':
        formaPersona = Personaform(request.POST,instance=persona)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('indexPersonas')
    else:
        formaPersona = Personaform(instance=persona)
    return render(request,'editar.html',{'formaPersona':formaPersona})

def eliminarPersona(request, id):
    persona = get_object_or_404(Persona,pk=id)
    if persona:
        persona.delete()
    return redirect('indexPersonas')

def detallePersona(request,id):
    persona = get_object_or_404(Persona,pk=id)
    return render(request,'detalle.html',{'persona':persona})