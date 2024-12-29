from django.urls import path
from .views import blog_list_view

app_name = 'blog'

urlpatterns = [
    path('', blog_list_view, name='list'),
]
