from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='game-home'),
    path('about/', views.home, name='game-about'),
]