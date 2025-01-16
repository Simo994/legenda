from django.urls import path
from . import views

urlpatterns = [
    # Основные страницы
    path('', views.home, name='home'),
    
    # Бронирование
    path('reservation/', views.reservation, name='reservation'),
    path('reservation/success/', views.reservation_success, name='reservation_success'),
    
    # Регистрация
    path('register/', views.register, name='register'),
]
