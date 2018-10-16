<<<<<<< HEAD
from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('catalog/submit', views.submitPage, name='submitpage'),
    path('posts/', views.postPage, name='postspage'),
    path('storage/', views.storage, name = 'storage'),
]
=======
from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('catalog/submit', views.submitPage, name='submitpage'),
    path('posts/', views.postPage, name='postspage'),
    path('storage/', views.storage, name = 'storage'),
]
>>>>>>> 22a6091a491fe2054f85be42c1737e25844e20ab
