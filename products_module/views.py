from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters import rest_framework as filters
from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer

class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    category = filters.CharFilter(field_name="category")

    class Meta:
        model = Product
        fields = ['category', 'min_price', 'max_price']

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_class = ProductFilter

    @action(detail=True, methods=['post'])
    def add_to_cart(self, request, pk=None):
        try:
            product = self.get_object()
            # Add cart logic here
            return Response({'status': 'Product added to cart'})
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

def product_page(request):
    return render(request, 'products_module/products.html')

def products(request):
    products = Product.objects.filter(is_available=True)
    return render(request, 'products_module/products.html', {'products': products})
