from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='categories/')  # Assuming you have an "categories" directory in your MEDIA_ROOT
    status = models.BooleanField(default=True)  # Checkbox for status
    trending = models.BooleanField(default=False)  # Checkbox for trending

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return self.name
    
    def get_url(self):
        return reverse('e_commerceApp:products_by_cat', args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='products/')  # Assuming you have an "products" directory in your MEDIA_ROOT
    description = models.TextField()
    quantity = models.IntegerField(default=0)
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=True)  # Checkbox for status
    trending = models.BooleanField(default=False)  # Checkbox for trending

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'
        
    def __str__(self):
        return self.name
    
    def get_url(self):
        return reverse('e_commerceApp:proDetailName', args=[self.category.slug,self.slug])
