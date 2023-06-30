from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *

menu = [{'title': "Главная", 'url_name': 'home'},
        {'title': "Нарушения", 'url_name': 'violation'},
        {'title': "Происшествия", 'url_name': 'incident'}
]

def index(request):
    
    return render(request, 'ohrana/index.html', {'menu':menu, 'title':'Главная'})

def violation(request):
    posts = Sluzhebnaya_zapiska.objects.all()
    return render(request, 'ohrana/violation.html', {'posts':posts, 'menu':menu, 'title':'Нарушения'})

def incident(request):
    
    return render(request, 'ohrana/incident.html', {'menu':menu, 'title':'Происшествия'})

def show_post(request, post_id):
  
    return render(request, 'ohrana/cz.html', {'menu':menu, 'title':'Оформление'})

# def CZ(request, name):
#     if (request.GET):
#         print(request.GET)
#     return HttpResponse(f'Вторая страница {name}')

# def arhive(request, year):
#     return HttpResponse(f'Третья страница')