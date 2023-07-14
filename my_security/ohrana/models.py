from django.db import models
from django.urls import reverse

# Create your models here.

class Sluzhebnaya_zapiska(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="", blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})
    
    class Meta:
        verbose_name = "Служебные записки"
        verbose_name_plural = "Служебные записки"
        ordering = ['time_create', 'title']


class My_Incid(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    content_1 = models.TextField(blank=True)
    content_2 = models.TextField(blank=True)
    content_3 = models.TextField(blank=True)
    content_4 = models.TextField(blank=True)
    content_5 = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title        
    
    def get_absolute_url(self):
        return reverse('postic', kwargs={'post_id': self.pk})