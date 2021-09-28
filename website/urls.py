from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'website'

urlpatterns = [
    path("", views.homepage, name = "homepage"),
    path("homepage", views.homepage, name = "homepage"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("about", views.about, name="about"),
    path("add_review", views.add_review, name="add_review"),
    path("movie_details/<int:show_id>",views.movie_details, name="movie_details"),
    path("add_movie", views.add_movie, name="add_movie")
]