from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product, Style, SimilarItem, Photo

admin.site.register(Product)
admin.site.register(Style)
admin.site.register(SimilarItem)
admin.site.register(Photo)