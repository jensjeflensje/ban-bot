from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home),
    path("invite/", views.invite),
    path("discord/", views.discord),
    path("info/maker/", views.maker),
    path("info/bot/", views.bot),
    path("user/<int:user_id>/", views.search_user),
    path("search/", views.search),
]
