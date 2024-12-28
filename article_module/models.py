from django.db import models

# Create your models here.

class ArticleCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name='Category Title')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='Children', on_delete=models.SET_NULL)
    slug = models.SlugField(max_length=200, blank=True, db_index=True, unique=True, verbose_name='URL In Category Title')

    class Meta:
        verbose_name = 'Article Category'
        verbose_name_plural = 'Article Categories'

    def __str__(self) -> str:
        return self.title
                
    
class Articles(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    short_description = models.CharField(max_length=350, verbose_name='Short Description')
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(upload_to='images/articles', verbose_name='Image Article')
    slug = models.SlugField(max_length=200, blank=True, db_index=True, unique=True, verbose_name='URL In Title')
    is_active = models.BooleanField(default=True, verbose_name='Active')
    categories = models.ManyToManyField(ArticleCategory, verbose_name='Categories')
    ceated_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Date and Time')

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self) -> str:
        return self.title
    


#NOTE:ARTICLES COMMENT

    


