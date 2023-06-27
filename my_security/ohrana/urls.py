from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('CZ/<str:name>/', CZ),
]