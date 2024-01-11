from django.contrib.auth.models import User
from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=25)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=120)
    date = models.DateField()
    is_available = models.BooleanField()
    # cats = models.ManyToManyField('Categories')

    def __str__(self):
        return self.name

class Categories(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey('Products', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()
    full_price = models.PositiveIntegerField()