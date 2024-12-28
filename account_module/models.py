from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Add any additional fields if needed
    pass

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self) -> str:
        return self.username