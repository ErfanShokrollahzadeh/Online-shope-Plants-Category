from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.


def indexhome(request):
    return render(request, 'home_module/index.html')