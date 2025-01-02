from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_module.urls')),
    path('account/', include('account_module.urls', namespace='account_module')),  # Add namespace here
]
