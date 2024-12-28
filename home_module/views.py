from django.shortcuts import render
from django.http import HttpRequest
from .models import HeroSection, PlantBenefit

# Create your views here.


def indexhome(request):
    hero = HeroSection.objects.first()
    benefits = PlantBenefit.objects.all()
    
    # Default images
    default_hero_image = 'https://source.unsplash.com/random/1600x900/?plants'
    default_benefit_image = 'https://source.unsplash.com/random/400x300/?plant'
    
    return render(request, 'home_module/index.html', {
        'hero': hero,
        'benefits': benefits,
        'default_hero_image': default_hero_image,
        'default_benefit_image': default_benefit_image,
    })