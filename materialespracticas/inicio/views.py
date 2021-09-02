from django.shortcuts import render, get_object_or_404, redirect
from .models import Empleado
from .models import Materiales 
from .forms import MaterialesForm

# Create your views here.

def registro_empleados(request):
    
    empleados = Empleado.objects.all()
    data = {
        'empleados':empleados
    }
    return render(request, "inicio/registro_empleados.html", data) 

def inicio(request):
    return render(request, "inicio/inicio.html")

def pricipal(request):
    materiales = Materiales.objects.all()
    return render(request, "inicio/principal.html",{'materiales':materiales})

def form(request):
    data ={
        'form ': MaterialesForm()
    }
    if request.method == 'POST':
        form = MaterialesForm(data=request.POST)
        if form.is_valid():
            form.save()
            data["mensaje"]="Guardado"
            materiales = Materiales.objects.all()
            return render(request, "inicio/principal.html", {'materiales':materiales})
        else:
            data["mensaje"] = "Debes enviar todos los campos llenos"
    return render(request, "inicio/form.html", data)

def editar(request, id):
    
    material = get_object_or_404(Materiales, id=id)
    data = {
        'form': MaterialesForm(instance=material)
    }

    if request.method == 'POST':
        form = MaterialesForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            return redirect(to='principal')
        data["form"]=form  

    return render(request, "inicio/edicion.html", data)

def eliminar(request, id):
    material = get_object_or_404(Materiales, id=id)
    material.delete()
    return redirect(to='principal')
    
