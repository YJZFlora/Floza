from django.urls import path

from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.homePage, name="homePage"),
    path("makeOrder", views.index, name="makeOrder"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("user", views.user, name="user"),
    path("register", views.register, name="register"),
    path("checkout", views.checkout, name="checkout"),
    path("history", views.history, name="history")
]
