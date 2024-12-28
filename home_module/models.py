from django.db import models

class HeroSection(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    hero_image = models.ImageField(upload_to='hero/')
    
    def __str__(self):
        return self.title

class PlantBenefit(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_class = models.CharField(max_length=50, help_text="Bootstrap icon class (e.g., bi-tree)")
    image = models.ImageField(upload_to='benefits/')
    
    def __str__(self):
        return self.title
