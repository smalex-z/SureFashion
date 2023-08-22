from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("wardrobe/", views.wardrobe, name="wardrobe")
]