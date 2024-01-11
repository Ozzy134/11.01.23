from django.urls import path
from .views import ProductsGet

urlpatterns = [
    path('products/', ProductsGet.as_view()),
    path('products/<int:pk>/', ProductsGet.as_view())
]