# Generated by Django 4.2.2 on 2023-07-14 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ohrana', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='my_incid',
            name='content_6',
        ),
    ]