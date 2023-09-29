from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Product
from . import serializers


class ProductListAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = serializers.ProductSerializer(products, many=True)
        return Response({"access": True, "data": serializer.data})
    

class ProductDetailAPIView(APIView):
    def get(self, request, id):
        product = get_object_or_404(Product, id=id)
        serializer = serializers.ProductSerializer(product)
        return Response({"access": True, "data": serializer.data})


class ProductCreateAPIView(APIView):
    def post(self, request):
        serializer = serializers.ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"access": True, "data": serializer.data})
        return Response({"access": False, "data": serializer.errors})
        

class ProductUpdateAPIView(APIView):
    def put(self, request, id):
        product = get_object_or_404(Product, id=id)
        serializer = serializers.ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"access": True, "data": serializer.data})
        return Response({"access": False, "data": serializer.errors})
        
    
class ProductDeleteAPIView(APIView):
    def delete(self, request, id):
        product = get_object_or_404(Product, id=id)
        product.delete()
        return Response({"access": True, "message": "Product deleted successfully."})
        
