from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    first_name = None
    last_name = None
    username = models.CharField(max_length=50, unique=True, verbose_name='Username')
    avatar = models.ImageField(upload_to='images/profiles', blank=True, null=True, verbose_name='Image Avatar')
    email_active_code = models.CharField(max_length=200, verbose_name='Active Code')
    

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self) -> str:
        return self.username