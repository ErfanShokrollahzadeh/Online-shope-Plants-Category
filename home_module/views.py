from django.shortcuts import render
from django.http import HttpRequest
from .models import HeroSection, PlantBenefit

# Create your views here.


def indexhome(request):
    hero = HeroSection.objects.first()
    benefits = PlantBenefit.objects.all()
    return render(request, 'home_module/index.html', {
        'hero': hero,
        'benefits': benefits,
    })