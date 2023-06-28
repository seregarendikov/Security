from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index),
    path('violation', violation),
    path('incident', incident),
    path('CZ/<str:name>/', CZ),
    re_path(r'^arhive/(?P<year>[0-9]{4})/', arhive)

]