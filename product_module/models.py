from django.db import models
from account_module.models import User

# Create your models here.

class ProductCategory(models.Model):
    title = models.CharField(max_length=80, db_index=True, verbose_name='Title Category')
    url_title = models.CharField(max_length=200, db_index=True, verbose_name='URL Title Category')
    is_active = models.BooleanField(verbose_name='Active Category')
    is_delete = models.BooleanField(verbose_name='Delete category')

    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'

    def __str__(self) -> str:
        return f'({self.title} - {self.url_title})'
    

class Product(models.Model):
    title = models.CharField(max_length=80, db_index=True, verbose_name='Product')
    category = models.ManyToManyField(ProductCategory, related_name='product_category', verbose_name='Product Categories')
    image = models.ImageField(upload_to='images/products', null=True, blank=True, verbose_name='Product Photo')
    price = models.IntegerField(verbose_name='Price')
    short_description = models.CharField(max_length=350, null=True ,db_index=True, verbose_name='Short Description')
    description = models.TextField(db_index=True, verbose_name='Description')
    slug = models.SlugField(max_length=200, default='', null=False, blank=True, unique=True, db_index=True, verbose_name='URL Title')
    is_active = models.BooleanField(verbose_name='Active Product')
    is_delete = models.BooleanField(verbose_name='Delete Product')


    #NOTE:get absolute url and save metode

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self) -> str:
        return f'{self.title} - ({self.price})'
    

class ProductVisit(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name='IP Address')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Timestamp')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product')
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, verbose_name='User')

    class Meta:
        verbose_name = 'Product Visit'
        verbose_name_plural = 'Product Visits'

    def __str__(self) -> str:
        return f'{self.product.title} / {self.ip_address}'