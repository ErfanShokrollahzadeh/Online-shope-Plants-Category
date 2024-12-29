from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'account_module'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]
