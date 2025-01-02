from django.db import models

# Create your models here.

class ContactUs(models.Model):
    full_name = models.CharField(max_length=80, verbose_name='Full Name')
    title = models.CharField(max_length=100, verbose_name='Title')
    email = models.EmailField(max_length=254, verbose_name='Email')
    message = models.TextField(verbose_name='Message')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Create Date')
    response = models.TextField(null=True, blank=True, verbose_name='Response')
    is_resolved = models.BooleanField(default=False, verbose_name='Resolved')

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self) -> str:
        return f'{self.full_name} - {self.email}'