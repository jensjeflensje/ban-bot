from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home),
    path("search/", views.search),
    path("user/<int:user_id>/", views.search_user),
]
