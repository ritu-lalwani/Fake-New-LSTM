from rest_framework import viewsets
from .serializers import MovieDetailsSerializer
from .models import MovieDetails
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
import requests

# class MovieDetailsViewSet(viewsets.ModelViewSet):
#     queryset = MovieDetails.objects.all().order_by('place')
#     serializer_class = MovieDetailsSerializer

@api_view(['GET'])
def showMovies(request):
    if request.method == 'GET':
        results = MovieDetails.objects.all()
        serialize = MovieDetailsSerializer(results,many=True)
        return Response(serialize.data)

def displayData(request):
    callapi = requests.get('http://127.0.0.1:8000/movies/')
    results = callapi.json()
    render(request,'image.html',{'MovieDetails':results})
    return render(request,'index.html',{'MovieDetails':results[0:16]})