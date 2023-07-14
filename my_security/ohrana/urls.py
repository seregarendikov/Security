from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('violation', violation, name='violation'),
    path('incident', incident, name='incident'),
    path('violation/<int:post_id>/', show_post, name='post'),
    path('incident/<int:post_id>/', show_incid, name='postic'),




    # path('CZ/<str:name>/', CZ),
    # re_path(r'^arhive/(?P<year>[0-9]{4})/', arhive)

]