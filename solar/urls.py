from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view, name='home' ),
    path('about/',views.about_view, name='about'),
    path('blog/',views.blog_view, name='blog'),
    path('contact/',views.contact_view, name='contact'),
    path('project/',views.project_view, name='project'),
    path('team/',views.team_view, name='team'),
    path('services/',views.services_view, name='services'),
    
    ]