from django.contrib import admin
from .models import Persona, Skills, Post

# Register your models here.
admin.site.register([Persona, Skills, Post])
