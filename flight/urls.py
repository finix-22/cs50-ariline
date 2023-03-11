from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:flight_id>", views.flight_view, name="flight_view"),
    path("<int:flight_id>/book", views.book, name="book"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout")
]