from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, product_page

router = DefaultRouter()
router.register(r'api/products', ProductViewSet)

app_name = 'products'

urlpatterns = [
    path('', product_page, name='list'),
    path('', include(router.urls)),
]
