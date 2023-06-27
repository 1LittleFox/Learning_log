"""Определяет схемы URL для пользоваателей"""

from django.urls import path, include  # for login page
from . import views  # for registration page

app_name = 'users'

urlpatterns = [
    # Include the default authentication urls
    path('', include('django.contrib.auth.urls')),

    path('logout', views.logout_view, name='logout'),

    path('register/', views.register, name='register')
]