from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('posts/', views.postPage, name='postspage')
    #path('frontpage/', views.frontpage, name='frontpage')
]
