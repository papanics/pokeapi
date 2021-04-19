from rest_framework import serializers
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PokemonSerializer

from pokemon_app.models import Pokemon




@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/pokemon-list',
        'Detail View': '/pokemon-detail/<str:pk>/',
        'Create': '/pokemon-create/',
        'Update': '/pokemon-update/<str:pk>',
        'Delete': '/pokemon-delete<str:pk>',
    }


    return Response(api_urls)

@api_view(['GET'])
def pokemonList(request):
    pokemon = Pokemon.objects.all()
    serializer = PokemonSerializer(pokemon, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def pokemonDetail(request, pk):
    pokemon = Pokemon.objects.get(id=pk)
    serializer = PokemonSerializer(pokemon, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def pokemonCreate(request):
    serializer = PokemonSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def pokemonUpdate(request, pk):
    pokemon = Pokemon.objects.get(id=pk)
    serializer = PokemonSerializer(instance=pokemon, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def pokemonDelete(request, pk):
    pokemon = Pokemon.objects.get(id=pk)
    pokemon.delete()
 

    return Response('Item successfully deleted!')
