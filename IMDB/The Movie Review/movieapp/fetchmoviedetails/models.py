from django.db import models
from django.forms import ModelForm, Textarea

class MovieDetails(models.Model):
    place = models.IntegerField(primary_key=True)
    movie_title = models.CharField(max_length=255)
    year = models.IntegerField()
    star_cast = models.CharField(max_length=255)
    rating = models.FloatField()
    vote = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    images = models.CharField(max_length=255, blank=True, null=True)

class Meta:
    db_table = 'movie_details'

    # def __str__(self):
    #     return self.name
