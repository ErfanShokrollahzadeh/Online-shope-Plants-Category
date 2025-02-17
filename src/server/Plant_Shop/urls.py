"""
URL configuration for Plant_Shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_module.urls')),
    path('api/', include('products_module.urls')),
    path('account/', include('account_module.urls')),
    path('about/', include('about_module.urls', namespace='about')),
    path('contact/', include('contact_module.urls', namespace='contact')),
    path('blog/', include('blog_module.urls', namespace='blog')),
    path('products/', include('products_module.urls', namespace='products')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
