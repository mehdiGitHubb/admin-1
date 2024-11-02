from django.urls import path
from . import views

urlpatterns = [
    path('api/hero/', views.get_hero, name='get_hero'), 
    path('api/about_me/', views.get_about_me, name='get_about_me'),
    path('api/skills/', views.get_skills, name='get_skills'), 
    path('api/logos/', views.get_logo, name='get_logos'), 
    path('api/services/', views.get_services, name='get_services'), 
    path('api/works/', views.get_works, name='get_works'), 
    path('api/contacts/', views.get_contact, name='get_contact'), 



      # Ensure this line exists
]
