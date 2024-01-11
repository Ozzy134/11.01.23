from django.urls import path
from .views import CarsList, CarView, CarView2, FilmList, FilmView, FilmUpdate, FilmDel

urlpatterns = [
    path('cars', CarsList.as_view()),
    path('cars/<int:pk>', CarView.as_view()),
    path('cars/2/<int:pk>', CarView2.as_view()),
    path('films', FilmList.as_view()),
    path('films/<int:pk>', FilmView.as_view()),
    path('films/update/<int:pk>', FilmUpdate.as_view()),
    path('films/destroy/<int:pk>', FilmDel.as_view()),
]