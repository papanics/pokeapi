from django.urls import path
from . import views


urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
    path('pokemon-list/', views.pokemonList, name="pokemon-list"),
    path('pokemon-detail/<str:pk>/', views.pokemonDetail, name="pokemon-detail"),
    path('pokemon-create/', views.pokemonCreate, name="pokemon-create"),
    path('pokemon-update/<str:pk>/', views.pokemonUpdate, name="pokemon-update"),
    path('pokemon-delete/<str:pk>/', views.pokemonDelete, name="pokemon-delete"),
]