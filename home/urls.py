from . import views

from django.urls import path, include

#Put any new pages you create here.
urlpatterns = [
    path("", views.home, name="home"),                                  #homepage
    path("wardrobe/", views.wardrobe, name="wardrobe"),                 #Wardrobe
    path('auth/', views.authentication_view, name='authentication'),    #authentication page for Login/Signup
    path('logout/', views.logout_view, name='logout'),                  #URL used to logout, quickly redirected to home
    path('inspiration/', views.inspiration, name= "inspiration"),       #Inspiration
    path('admin_items/', views.admin_items, name='admin_items'),        #Admin page to view Similar items
    path('admin_styles/', views.admin_styles, name='admin_styles'),     #Admin page to view styles
    path('auth/', include('social_django.urls', namespace='social')),  # Include social-auth URLs here

]

