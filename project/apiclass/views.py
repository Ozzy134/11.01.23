from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveDestroyAPIView, UpdateAPIView, DestroyAPIView
from .models import Cars, Film
from .serializers import CarsSerializers, FilmSerializers
from rest_framework.permissions import IsAdminUser

class CarsList(ListCreateAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializers

class CarView(RetrieveAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializers
    permission_classes = [IsAdminUser]

class CarView2(RetrieveDestroyAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializers
#
# sdfsdfsdfsdfsdfsdfsfsdfsdfsdf

class FilmList(ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializers

class FilmView(RetrieveAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializers

class FilmUpdate(UpdateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializers

class FilmDel(DestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializers