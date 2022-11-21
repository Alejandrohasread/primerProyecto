from django.shortcuts import render
from django.http import HttpResponse
from .models import usuariosDjango
# Create your views here.


def index(request):
    return HttpResponse('Esta es mi primera vista')

def ingreso(request):
    usuariosInformacion = usuariosDjango.objects.all().order_by('id')
    if request.method == 'POST':
        if 'Crear' in request.POST:
            nuevoUsuario=[]
            print('Hola, se ha posteado información') 
            nombre = request.POST.get('nombreUsuario')
            apellido = request.POST.get('apellidoUsuario')
            edad = request.POST.get('edadUsuario')
            print('El nombre del usuario es : ' + str(nombre) )
            print('El apellido del usuario es : ' + str(apellido) )
            print('La edad del usuario es : ' + str(edad) )
            nuevoUsuario.append(str(nombre))
            nuevoUsuario.append(str(apellido))
            nuevoUsuario.append(str(edad))
            usuariosDjango(nombre=str(nombre),apellido=str(apellido),edad=str(edad)).save()
            usuariosInformacion = usuariosDjango.objects.all().order_by('id')    
        elif 'Filtrar' in request.POST:
            filtradoEdad = request.POST.get('edadFiltrado')
            usuariosInformacion = usuariosDjango.objects.filter(edad=filtradoEdad)
    return render(request,'ejemplo_django/ingreso.html',{
        'usuarios': usuariosInformacion,
        })
    