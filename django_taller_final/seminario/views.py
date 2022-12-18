from django.shortcuts import render
from seminario.models import Seminario
from seminario.forms import FormSeminario
# Create your views here.

def index(request):
    return render(request, 'index.html')

def opciones(request):
    return render(request, 'opciones.html')

#registrar datos del formulario en la base de datos 
def registrar(request):
    form = FormSeminario()
    if request.method == 'POST':
        print(request.POST)
        form = FormSeminario(request.POST)
        if (form.is_valid()):
            print(form)
            form.save()
        return index(request)
    data = {'form':form}
    return render(request, 'registrar.html', data)

#funcion para listar los datos de la base de datos
def listar(request):
    seminarios=Seminario.objects.all()
    data = {'seminarios':seminarios}
    return render(request, 'listar.html', data)

def editar(request, id):
    if request.method == 'GET':
        seminario = Seminario.objects.get(id=id)
        form = FormSeminario(instance=seminario)
        data = {'form':form}
        return render(request, 'editar.html', data)
    else:
        try:
            seminario = Seminario.objects.get(id=id)
            form = FormSeminario(request.POST, instance=seminario)
            if form.is_valid():
                form.save()
            return listar(request)
        except ValueError:
            return render(request, 'editar.html', {'form':form, 'error':'Error al editar'})
        
def eliminar(request, id):
    seminario = Seminario.objects.get(id=id)
    seminario.delete()
    return listar(request)
    

