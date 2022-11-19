from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

lista_elementos = [['Javier','Hilario','35'],['Dante','Arroyo','32'],['Luis','Velazco','33']]

def index(request):
    return HttpResponse('Esta es mi primera vista')

def ingreso(request):
    if request.method == 'POST':
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
        lista_elementos.append(nuevoUsuario)
    return render(request,'ejemplo_django/ingreso.html',{
        'usuarios': lista_elementos,
        })
    