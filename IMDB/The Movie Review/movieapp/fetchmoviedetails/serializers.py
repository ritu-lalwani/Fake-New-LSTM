from rest_framework import serializers

from .models import MovieDetails

class MovieDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieDetails
        fields = '__all__'