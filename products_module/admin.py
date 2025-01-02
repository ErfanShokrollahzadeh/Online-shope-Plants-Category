from django.contrib import admin
from .models import Product, ProductCategory

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'created_at']
    list_filter = ['is_active']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock', 'is_active', 'is_featured']
    list_filter = ['category', 'is_active', 'is_featured']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['price', 'stock', 'is_active', 'is_featured']
    fieldsets = (
        ('Basic Information', {
            'fields': ('category', 'name', 'slug', 'description', 'price', 'image')
        }),
        ('Stock Information', {
            'fields': ('stock', 'is_active', 'is_featured')
        }),
        ('Plant Care Details', {
            'fields': ('care_instructions', 'plant_size', 'light_requirement', 'watering_frequency'),
            'classes': ('collapse',)
        })
    )