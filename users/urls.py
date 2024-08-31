"""Определяет схемы URL для пользователей"""
from django.urls import path, include
from . import views


app_name = 'users'
urlpatterns = [
    # Включить URL авторизации по умолчанию.
    path('', include('django.contrib.auth.urls')),
    path(r"^logout/$", views.logout_user, name='logout'),
    # Страница авторицации
    path('register/', views.register, name='register'),
]