from django.db import models

class HeroSection(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    hero_image = models.ImageField(upload_to='hero/', blank=True, null=True)
    
    def __str__(self):
        return self.title

class PlantBenefit(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_class = models.CharField(max_length=50, help_text="Bootstrap icon class (e.g., bi-tree)")
    image = models.ImageField(upload_to='benefits/', blank=True, null=True)
    
    def __str__(self):
        return self.title

class Slider(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField(blank=True)
    image = models.ImageField(upload_to='sliders/')
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
