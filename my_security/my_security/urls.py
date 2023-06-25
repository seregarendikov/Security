from django.contrib import admin
from django.urls import path, include
# from ohrana.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ohrana/', include('ohrana.urls')),
]
