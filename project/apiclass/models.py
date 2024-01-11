from django.contrib.auth.models import User
from django.db import models

class Cars(models.Model):
    parts = models.ManyToManyField('Parts')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    sts = models.CharField(max_length=10)
    color = models.CharField(choices=[('red', 'red'), ('blue', 'blue'), ('yellow', 'yellow'),
                                      ('black', 'black'), ('white', 'white')], max_length=6)
    car = models.ForeignKey('CarsModels', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.car.name}, Owner {self.owner.username}'

class Parts(models.Model):
    part = models.CharField(max_length=100)

    def __str__(self):
        return self.part


class CarsModels(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

# fdvgfsgfdbfdb

class Film(models.Model):
    name = models.CharField(max_length=25)
    year = models.IntegerField()
    country = models.CharField(max_length=25)
    director = models.ForeignKey('Director', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=25)
    year = models.DateField()

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Poster(models.Model):
    date = models.DateField()
    film = models.ForeignKey('Film', on_delete=models.CASCADE)

    def __str__(self):
        return self.film.name

