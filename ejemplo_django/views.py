from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Esta es mi primera vista')

def ingreso(request):
    return render(request,'ejemplo_django/ingreso.html')
    