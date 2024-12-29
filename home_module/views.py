from django.shortcuts import render
from django.http import HttpRequest
from .models import HeroSection, PlantBenefit, Slider

# Create your views here.


def index(request):
    context = {
        'sliders': Slider.objects.filter(is_active=True).order_by('order'),
        'hero': HeroSection.objects.first(),
        'benefits': PlantBenefit.objects.all(),
        'default_hero_image': '/static/images/default-hero.jpg',
        'default_benefit_image': '/static/images/default-benefit.jpg',
        'default_slider_image': '/static/images/default-slider.jpg',
    }
    return render(request, 'home_module/index.html', context)