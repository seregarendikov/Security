from django.contrib import admin
from .models import Sluzhebnaya_zapiska, My_Incid



class Sluzhebnaya_zapiskaAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'time_create']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'content']


admin.site.register(Sluzhebnaya_zapiska, Sluzhebnaya_zapiskaAdmin)

class My_IncidAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content_1', 'time_create']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'content_1']


admin.site.register(My_Incid, My_IncidAdmin)
