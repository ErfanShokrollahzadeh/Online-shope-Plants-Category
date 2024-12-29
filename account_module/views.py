from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings
from .social_auth import get_social_auth_urls
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.db import transaction

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
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = form.save()
                    login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                    messages.success(request, 'Account created successfully!')
                    return redirect('home')
            except Exception as e:
                messages.error(request, f'Error creating account: {str(e)}')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{error}')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'account_module/signup.html', {'form': form})
