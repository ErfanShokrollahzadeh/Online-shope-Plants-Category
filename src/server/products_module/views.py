from django.views.generic import DetailView, ListView
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product, ProductCategory
from .serializers import ProductSerializer, ProductDetailSerializer

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.filter(is_active=True, is_delete=False)
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'light_requirement', 'plant_size']
    search_fields = ['title', 'description']
    ordering_fields = ['price', 'created_at']
    template_name = None  # Disable template rendering for API view

    def get_template_names(self):
        return []  # Return empty list to prevent template lookup

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.filter(is_active=True, is_delete=False)
    serializer_class = ProductDetailSerializer
    lookup_field = 'slug'

# Frontend Views
class ProductListView(ListView):
    model = Product
    template_name = 'products_module/product_list.html'
    context_object_name = 'products'
    queryset = Product.objects.filter(is_active=True, is_delete=False)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products_module/product_detail.html'
    context_object_name = 'product'
    lookup_field = 'slug'
