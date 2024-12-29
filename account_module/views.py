from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.conf import settings
from .social_auth import get_social_auth_urls

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    context = {
        'backends': {
            'google': True,
            'facebook': True
        },
        'social_urls': get_social_auth_urls()
    }
    return render(request, 'account_module/login.html', context)

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    
    context = {
        'backends': {
            'google': True,
            'facebook': True
        },
        'social_urls': get_social_auth_urls()
    }
    return render(request, 'account_module/signup.html', context)
