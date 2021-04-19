from django.db import models
from rest_framework import serializers
from rest_framework.utils import field_mapping
from pokemon_app.models import Pokemon
class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = '__all__'