from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginForm, name='login'),
    path('register/', views.registerForm, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('feedback/',views.feedback, name='feedback'),
    path('view_feedback/',views.view_feedback, name='view_feedback'),
    path('event/',views.event, name='event'),
    path('announcement/',views.announcement, name='announcement'),
]