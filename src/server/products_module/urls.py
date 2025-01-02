from django.urls import path
from . import views

app_name = 'products_module'

# Split URL patterns for better organization
api_urlpatterns = [
    path('products/', views.ProductListAPIView.as_view(), name='product-list-api'),
    path('products/<slug:slug>/', views.ProductDetailAPIView.as_view(), name='product-detail-api'),
]

frontend_urlpatterns = [
    path('', views.ProductListView.as_view(), name='product-list'),
    path('<slug:slug>/', views.ProductDetailView.as_view(), name='product-detail'),
]

urlpatterns = api_urlpatterns + frontend_urlpatterns