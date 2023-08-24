from . import views

from django.urls import path


urlpatterns = [
    path("", views.home, name="home"),
    path("wardrobe/", views.wardrobe, name="wardrobe"),
    path('auth/', views.authentication_view, name='authentication'),
    path('logout/', views.logout_view, name='logout'),
]

