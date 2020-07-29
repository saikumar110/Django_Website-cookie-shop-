from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index,name="index"),
    path('about', views.about,name="about"),
    path('contact', views.Contactsss,name="contact"),
    path('menu', views.Menu,name="menu"),
    path('archive', views.Archieve,name="archive"),
]