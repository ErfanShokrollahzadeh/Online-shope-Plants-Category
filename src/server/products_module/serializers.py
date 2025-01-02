from rest_framework import serializers
from .models import Product, ProductCategory

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'title', 'url_title']

class ProductSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer(read_only=True)
    
    class Meta:
        model = Product
        fields = [
            'id', 'title', 'category', 'price', 
            'short_description', 'slug', 'image',
            'light_requirement', 'plant_size'
        ]

class ProductDetailSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer(read_only=True)
    
    class Meta:
        model = Product
        fields = [
            'id', 'title', 'category', 'price',
            'short_description', 'description', 'slug',
            'image', 'light_requirement', 'watering_frequency',
            'plant_size', 'care_instructions', 'created_at'
        ]
