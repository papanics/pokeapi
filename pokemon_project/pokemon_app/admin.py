from django.contrib import admin
from .models import Pokemon


@admin.register(Pokemon)
class Pokemon(admin.ModelAdmin):
    list_display = ('name', 'url')
    list_filter = ("name", )
    search_fields = ("name__startswith", )

