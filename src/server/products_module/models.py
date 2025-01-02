from django.db import models
from django.utils.text import slugify
from django.utils import timezone

class ProductCategory(models.Model):
    title = models.CharField(max_length=300, verbose_name='Title')
    url_title = models.CharField(max_length=300, unique=True, verbose_name='URL Title', null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='Active')
    is_delete = models.BooleanField(default=False, verbose_name='Deleted')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Product(models.Model):
    LIGHT_CHOICES = [
        ('low', 'Low Light'),
        ('medium', 'Medium Light'),
        ('high', 'High Light'),
    ]
    
    SIZE_CHOICES = [
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    ]
    
    title = models.CharField(max_length=300, verbose_name='Title',null=True, blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name='Category')
    price = models.IntegerField(verbose_name='Price')
    short_description = models.CharField(
        max_length=360, 
        verbose_name='Short Description',
        null=True,
        blank=True,
        default=''
    )
    description = models.TextField(verbose_name='Description')
    is_active = models.BooleanField(default=True, verbose_name='Active')
    is_delete = models.BooleanField(default=False, verbose_name='Deleted')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Slug')
    image = models.ImageField(upload_to='images/products', verbose_name='Image')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)
    
    # Updated fields with null=True and default values
    light_requirement = models.CharField(
        max_length=50, 
        choices=LIGHT_CHOICES, 
        verbose_name='Light Requirement',
        default='medium'
    )
    watering_frequency = models.CharField(
        max_length=100, 
        verbose_name='Watering Frequency',
        null=True, 
        blank=True
    )
    plant_size = models.CharField(
        max_length=50, 
        choices=SIZE_CHOICES, 
        verbose_name='Plant Size',
        default='medium'
    )
    care_instructions = models.TextField(
        verbose_name='Care Instructions',
        null=True, 
        blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
