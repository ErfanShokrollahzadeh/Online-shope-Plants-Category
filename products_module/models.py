from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('indoor', 'Indoor Plants'),
        ('outdoor', 'Outdoor Plants'),
        ('succulents', 'Succulents'),
        ('herbs', 'Herbs'),
        ('trees', 'Trees'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
