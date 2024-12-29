from django.contrib import admin
from .models import Product, ProductCategory, ProductVisit


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'is_active', 'is_delete']
    list_filter = ['is_active', 'is_delete', 'category']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'url_title', 'is_active', 'is_delete']
    list_filter = ['is_active', 'is_delete']
    search_fields = ['title']


@admin.register(ProductVisit)
class ProductVisitAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'ip_address', 'timestamp']
    list_filter = ['timestamp']
    search_fields = ['product__title', 'ip_address']
