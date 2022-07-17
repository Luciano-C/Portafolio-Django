from django.contrib import admin
from .models import Project

# Register your models here.
# Sirve para que los modelos en models.py aparezcan en el administrador
admin.site.register(Project)
