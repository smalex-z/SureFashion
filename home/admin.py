from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product, Style, SimilarItem

admin.site.register(Product)
admin.site.register(Style)
admin.site.register(SimilarItem)