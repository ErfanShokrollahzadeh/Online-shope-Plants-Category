from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'api/products', views.ProductViewSet)

app_name = 'products_module'

urlpatterns = [
    path('', views.product_page, name='list'),
    path('', include(router.urls)),
    path('products/', views.products, name='products'),
]
