from django.contrib import admin
from django.urls import path, include
from about_module.views import about_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('social_django.urls', namespace='social')),
    # ...existing code...
    path('about/', about_view, name='about'),
    # ...existing code...
]
