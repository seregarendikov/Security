from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    
    return HttpResponse('Главная страница')

def CZ(request, name):
    if (request.GET):
        print(request.GET)
    return HttpResponse(f'Вторая страница {name}')