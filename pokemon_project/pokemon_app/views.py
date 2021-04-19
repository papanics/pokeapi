from django.shortcuts import  render, redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import Pokemon
import requests
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


def get_pokemons(request):

    if 'load' in request.GET:
        name = request.GET.get('name')
        url = 'https://pokeapi.co/api/v2/pokemon?limit=151&offset=200 s=%s' % name
        response = requests.get(url)
        data = response.json()
        results = data['results']
        

        for i in results:
            pokemon_data = Pokemon(
                name = i['name'],
                url = i['url']
            )
            pokemon_data.save()
            messages.success(request, 'Successfully saved pokemons from the pokeapi ')
            return redirect('/pokemon')
            
            
    
    return render (request, 'pokemons/save_pokemon.html' )

class PokemonListView(ListView):
    model = Pokemon
    template_name = 'pokemons/pokemon.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'pokemons'
    ordering = ['-id']

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(name__icontains=query)
        else:
            object_list = self.model.objects.all()
        return object_list

class PokemonDetailView(DetailView):
    model = Pokemon
    template_name = "pokemons/pokemon_detail.html"

class PokemonCreateView(SuccessMessageMixin,CreateView):
    model = Pokemon
    fields = ['name', 'url']
    template_name = "pokemons/pokemon_create.html"
    success_url = '/pokemon'
    success_message = "%(name)s was created successfully!"


class PokemonUpdateView(SuccessMessageMixin,UpdateView):
    model = Pokemon
    fields = ['name', 'url']
    template_name = "pokemons/pokemon_edit.html"
    success_url = '/pokemon'
    success_message = "%(name)s was updated successfully!"


class PokemonDeleteView(SuccessMessageMixin,DeleteView):
    model = Pokemon
    fields = ['name', 'url']
    template_name = "pokemons/pokemon_delete.html"
    success_url = '/pokemon'
    success_message = "%(name)s was deleted successfully"

