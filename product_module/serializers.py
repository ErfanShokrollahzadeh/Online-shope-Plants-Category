from rest_framework import serializers
from .models import Product, ProductCategory

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'title', 'url_title', 'is_active']

class ProductSerializer(serializers.ModelSerializer):
    categories = ProductCategorySerializer(source='category', many=True, read_only=True)
    
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'slug', 'is_active', 'categories']
