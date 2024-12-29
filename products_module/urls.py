from django.urls import path
from . import views

app_name = 'products_module'

urlpatterns = [
    path('', views.products, name='products'),
]
