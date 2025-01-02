from django.db import models

# Create your models here.


class SiteSetting(models.Model):
    site_name = models.CharField(max_length=100, verbose_name='Name Website')
    site_url = models.URLField(max_length=200, verbose_name='URL Website')
    address = models.TextField(blank=True, verbose_name='Address')
    logo = models.ImageField(upload_to='images/site-setting/', blank=True, verbose_name='Logo')
    email = models.JSONField(default=list, blank=True, verbose_name='Email')
    copy_right = models.TextField(blank=True, verbose_name='Copy Right')
    phone = models.CharField(max_length=50, verbose_name='Phone')
    is_main_setting = models.BooleanField(verbose_name='First Setting')


    class Meta:
        verbose_name = 'Setting Website'
        verbose_name_plural = 'Setting'
    
    def __str__(self) -> str:
        return self.site_name
