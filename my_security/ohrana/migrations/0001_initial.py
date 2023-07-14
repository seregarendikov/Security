# Generated by Django 4.2.2 on 2023-07-14 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='My_Incid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('content_1', models.TextField(blank=True)),
                ('content_2', models.TextField(blank=True)),
                ('content_3', models.TextField(blank=True)),
                ('content_4', models.TextField(blank=True)),
                ('content_5', models.TextField(blank=True)),
                ('content_6', models.TextField(blank=True)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sluzhebnaya_zapiska',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('content', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Служебные записки',
                'verbose_name_plural': 'Служебные записки',
                'ordering': ['time_create', 'title'],
            },
        ),
    ]
