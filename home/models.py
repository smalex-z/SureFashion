from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


 
# Create your models here.

class SimilarItem(models.Model):
    name = models.CharField(max_length=200, default='n/a')
    primary_color = models.CharField(max_length=50, default='n/a')
    secondary_color = models.CharField(max_length=50, default='n/a')
    heat_index = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        default=5
    )
    # ... Other attributes

class Style(models.Model):
    name = models.CharField(max_length=200, default='n/a')
    similar_items = models.ManyToManyField(SimilarItem, related_name='styles')
    # ... Other attributes

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=200, default='n/a')
    price = models.DecimalField(max_digits=7, decimal_places=2, default=1.00)
    image = models.ImageField(upload_to='products/', default='products/default.jpg')
    date_added = models.DateTimeField(auto_now_add=True)
    primary_color = models.CharField(max_length=50, default="n/a")
    secondary_color = models.CharField(max_length=50, default="n/a")
    heat_index = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        default= 5
    )
    similar_item = models.ForeignKey(SimilarItem, on_delete=models.CASCADE, default=1, null=True)
    styles = models.ManyToManyField(Style, related_name='products')
    # ... Other attributes

    def __str__(self):
        return self.name
    
#TODO: add formality