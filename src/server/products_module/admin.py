from django.contrib import admin
from . import models

@admin.register(models.ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'url_title', 'is_active']
    list_editable = ['is_active']

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'is_active', 'category']
    list_editable = ['is_active']
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Main Information', {
            'fields': ('title', 'category', 'price', 'image', 'slug')
        }),
        ('Descriptions', {
            'fields': ('short_description', 'description')
        }),
        ('Plant Care', {
            'fields': ('light_requirement', 'watering_frequency', 'plant_size', 'care_instructions')
        }),
        ('Settings', {
            'fields': ('is_active', 'is_delete')
        }),
    )