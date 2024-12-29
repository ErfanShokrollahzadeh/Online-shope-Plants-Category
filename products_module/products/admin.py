from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'stock', 'is_active']
    list_filter = ['created_at', 'is_active']
    search_fields = ['title', 'description']
    list_editable = ['price', 'stock', 'is_active']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'price', 'stock', 'image')
        }),
        ('Content', {
            'fields': ('description',)
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
