from django.contrib import admin
from .models import Pokemon

admin.site.register(Pokemon)

admin.site.site_header = "POKEAPI"
