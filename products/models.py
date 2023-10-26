from django.db import models
from django.urls import reverse

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200,unique = True)
    subdirectory = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    
    
    
    class  Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name




class Products(models.Model):

    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="products")
    name = models.CharField(max_length=200)
    slug =models.SlugField(max_length=200,unique=True)
    Image = models.ImageField(upload_to="products/%Y/%M/%D/")
    description = models.TextField(max_length=200)
    price = models.PositiveIntegerField()
    availablity = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):

        return self.name



    def get_absolute_url(self):
        return reverse('products:product_detail', args=[self.slug])