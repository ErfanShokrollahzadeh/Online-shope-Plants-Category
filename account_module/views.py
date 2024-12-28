from django.shortcuts import render

def login_view(request):
    return render(request, 'account_module/login.html')

def signup_view(request):
    return render(request, 'account_module/signup.html')
