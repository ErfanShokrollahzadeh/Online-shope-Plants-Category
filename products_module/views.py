from rest_framework import viewsets
from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

def product_page(request):
    return render(request, 'products_module/products.html')
