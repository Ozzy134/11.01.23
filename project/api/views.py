from django.forms import model_to_dict
from .models import Products, Categories
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import date
from .serializers import ProductsSerializer

class ProductsGet(APIView):
    def get(self, request):
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response({'data': serializer.data})

class ProductsGet(APIView):
    def get(self, request):
        products = Products.objects.all().values()
        return Response({'data': products})

    def post(self, request):
        # new_product = Products.objects.create(
        #     name=request.data['name'],
        #     description=request.data['description'],
        #     price=request.data['price'],
        #     date=request.data['date'],
        #     is_available=request.data['is_available'],
        #
        # ),
        # new_product.save()
        serializer = ProductsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'product': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response('fsdfsffdsf')

        try:
            product = Products.objects.get(pk=pk)
        except:
            return Response('Опять проблемы')

        serializer = ProductsSerializer(data=request.data, instance=product)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'product': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response('fsdfsffdsf')

        try:
            product = Products.objects.get(pk=pk)
        except:
            return Response('Опять проблемы')
        product.delete()
        return Response('Products deleted')