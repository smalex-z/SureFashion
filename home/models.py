from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

PRIMARY_COLOR_CHOICES = [
    ('#000000', 'Black'),
    ('#808080', 'Grey'),
    ('#FFFFFF', 'White'),
    ('#800000', 'Maroon'),
    ('#FF0000', 'Red'),
    ('#FFC0CB', 'Pink'),
    ('#A52A2A', 'Brown'),
    ('#FFA500', 'Orange'),
    ('#FBCEB1', 'Apricot'),
    ('#808000', 'Olive'),
    ('#FFFF00', 'Yellow'),
    ('#F5F5DC', 'Beige'),
    ('#00FF00', 'Lime'),
    ('#008000', 'Green'),
    ('#98FB98', 'Mint'),
    ('#008080', 'Teal'),
    ('#00FFFF', 'Cyan'),
    ('#000080', 'Navy'),
    ('#0000FF', 'Blue'),
    ('#800080', 'Purple'),
    ('#E6E6FA', 'Lavender'),
    ('#FF00FF', 'Magenta'),
]

SECONDARY_COLOR_CHOICES = [
    ('n/a', 'None'),
    ('#000000', 'Black'),
    ('#808080', 'Grey'),
    ('#FFFFFF', 'White'),
    ('#800000', 'Maroon'),
    ('#FF0000', 'Red'),
    ('#FFC0CB', 'Pink'),
    ('#A52A2A', 'Brown'),
    ('#FFA500', 'Orange'),
    ('#FBCEB1', 'Apricot'),
    ('#808000', 'Olive'),
    ('#FFFF00', 'Yellow'),
    ('#F5F5DC', 'Beige'),
    ('#00FF00', 'Lime'),
    ('#008000', 'Green'),
    ('#98FB98', 'Mint'),
    ('#008080', 'Teal'),
    ('#00FFFF', 'Cyan'),
    ('#000080', 'Navy'),
    ('#0000FF', 'Blue'),
    ('#800080', 'Purple'),
    ('#E6E6FA', 'Lavender'),
    ('#FF00FF', 'Magenta'),
]


# Create your models here.
class Photo(models.Model):
    image = models.ImageField(upload_to='products/', default='products/default.png')

    def __str__(self):
        return str(self.image)

class SimilarItem(models.Model):
    name = models.CharField(max_length=200, default='n/a')
    category = models.CharField(max_length=50, choices=[('outerwear', 'Outerwear'), ('top', 'Top'), ('bottom', 'Bottom'), ('shoes', 'Shoes'), ('accessory', 'Accessory')], default='top')
    primary_color = models.CharField(max_length=50, choices=PRIMARY_COLOR_CHOICES, default='black')
    secondary_color = models.CharField(max_length=50, choices=SECONDARY_COLOR_CHOICES, default='n/a')
    image = models.ImageField(upload_to='products/', default='products/default.png')
    formality = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default= 1
    )
    heat_index = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        default=5
    )
    belt = models.BooleanField(default=False)
    fits = models.ManyToManyField('Photo', blank=True)

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
    image = models.ImageField(upload_to='products/', default='products/default.png')
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
    belt = models.BooleanField(default=False)
    similar_item = models.ForeignKey(SimilarItem, on_delete=models.CASCADE, default=None, null=True, blank=True)
    styles = models.ManyToManyField(Style, related_name='products', blank=True)
    # ... Other attributes

    def __str__(self):
        return self.name
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    image = models.ImageField(upload_to='profile_pics/', default='profile_pics/default.png')

    def __str__(self):
        return self.user.username

    
#TODO: Add a model for saved outfits
    