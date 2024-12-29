from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('social_django.urls', namespace='social')),
    path('', include('home_module.urls')),
    path('account/', include('account_module.urls')),
    path('about/', include('about_module.urls', namespace='about')),
]
