from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("<int:game_id>", views.game_page, name="game_page"),
    path('watchlist', views.watchlist, name="watchlist")
]