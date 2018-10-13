from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='frontpage-home'),
    path('about/', views.about, name='frontpage-about'),
]
