from django.urls import  path
from django.urls.conf import include
from . import views
from .views import (
    PokemonListView,
    PokemonDetailView,
    PokemonCreateView,
    PokemonUpdateView,
    PokemonDeleteView,
 
)

urlpatterns = [
    path('', views.get_pokemons, name = "get_pokemons"),
    path('pokemon', PokemonListView.as_view(), name = "pokemons_list"),
    path('pokemon/<int:pk>/', PokemonDetailView.as_view(), name='pokemon_detail'),
    path('create/', PokemonCreateView.as_view(), name='pokemon_create'),
	path('update/<int:pk>', PokemonUpdateView.as_view(), name='pokemon_update'),
	path('delete/<int:pk>', PokemonDeleteView.as_view(), name='pokemon_delete'),

    #path('pokemons/<int:id>/',views.pokemon_detail, name = "pokemon_detail")
]