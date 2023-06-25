from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    
    return HttpResponse('Главная страница')

def CZ(request):
    
    return HttpResponse('Вторая страница')