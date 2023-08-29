from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

PRIMARY_COLOR_CHOICES = [
    ('black', 'Black'),
    ('grey', 'Grey'),
    ('white', 'White'),
    ('maroon', 'Maroon'),
    ('red', 'Red'),
    ('pink', 'Pink'),
    ('brown', 'Brown'),
    ('orange', 'Orange'),
    ('apricot', 'Apricot'),
    ('olive', 'Olive'),
    ('yellow', 'Yellow'),
    ('beige', 'Beige'),
    ('lime', 'Lime'),
    ('green', 'Green'),
    ('mint', 'Mint'),
    ('teal', 'Teal'),
    ('cyan', 'Cyan'),
    ('navy', 'Navy'),
    ('blue', 'Blue'),
    ('purple', 'Purple'),
    ('lavender', 'Lavender'),
    ('magenta', 'Magenta'),
]

SECONDARY_COLOR_CHOICES = [
    ('n/a', 'None'),
    ('black', 'Black'),
    ('grey', 'Grey'),
    ('white', 'White'),
    ('maroon', 'Maroon'),
    ('red', 'Red'),
    ('pink', 'Pink'),
    ('brown', 'Brown'),
    ('orange', 'Orange'),
    ('apricot', 'Apricot'),
    ('olive', 'Olive'),
    ('yellow', 'Yellow'),
    ('beige', 'Beige'),
    ('lime', 'Lime'),
    ('green', 'Green'),
    ('mint', 'Mint'),
    ('teal', 'Teal'),
    ('cyan', 'Cyan'),
    ('navy', 'Navy'),
    ('blue', 'Blue'),
    ('purple', 'Purple'),
    ('lavender', 'Lavender'),
    ('magenta', 'Magenta'),
]


# Create your models here.

class SimilarItem(models.Model):
    name = models.CharField(max_length=200, default='n/a')
    category = models.CharField(max_length=50, choices=[('outerwear', 'Outerwear'), ('top', 'Top'), ('bottom', 'Bottom'), ('shoes', 'Shoes'), ('accessory', 'Accessory')], default='top')
    primary_color = models.CharField(max_length=50, choices=PRIMARY_COLOR_CHOICES, default='black')
    secondary_color = models.CharField(max_length=50, choices=SECONDARY_COLOR_CHOICES, default='n/a')
    image = models.ImageField(upload_to='products/', default='products/default.jpg')
    formality = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default= 1
    )
    heat_index = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        default=5
    )
    # ... Other attributes

    def __str__(self):
        return self.name

class Style(models.Model):
    name = models.CharField(max_length=200, default='n/a')
    similar_items = models.ManyToManyField(SimilarItem, related_name='styles')
    # ... Other attributes

    def __str__(self):
        return self.name

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=200, default='n/a')
    image = models.ImageField(upload_to='products/', default='products/default.jpg')
    date_added = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50, choices=[('top', 'Top'), ('bottom', 'Bottom'), ('shoes', 'Shoes'), ('accessory', 'Accessory')], default='top')
    primary_color = models.CharField(max_length=50, choices=PRIMARY_COLOR_CHOICES, default='black')
    secondary_color = models.CharField(max_length=50, choices=SECONDARY_COLOR_CHOICES, default='black')
    formality = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default= 1
    )
    heat_index = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        default= 5
    )
    similar_item = models.ForeignKey(SimilarItem, on_delete=models.CASCADE, default=1, null=True)
    styles = models.ManyToManyField(Style, related_name='products')
    # ... Other attributes
    #TODO: For pants, belt required?

    def __str__(self):
        return self.name
    