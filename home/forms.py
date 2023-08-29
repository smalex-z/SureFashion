from django import forms
from .models import Product, SimilarItem, PRIMARY_COLOR_CHOICES, SECONDARY_COLOR_CHOICES
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class ProductForm(forms.ModelForm):
    primary_color = forms.TypedChoiceField(choices=PRIMARY_COLOR_CHOICES, coerce=str)
    secondary_color = forms.TypedChoiceField(choices=SECONDARY_COLOR_CHOICES, coerce=str)
    class Meta:
        model = Product
        fields = ['name', 'image', 'category', 'primary_color', 'secondary_color', 'heat_index']