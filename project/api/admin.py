from django.contrib import admin
from .models import Products, Categories, Order

admin.site.register(Products)
admin.site.register(Categories)
admin.site.register(Order)