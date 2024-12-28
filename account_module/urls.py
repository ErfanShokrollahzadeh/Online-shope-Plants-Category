from django.urls import path
from . import views

app_name = 'account_module'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    # ...existing code...
]
