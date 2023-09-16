from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new/", views.new, name="new"),
    path("categories/", views.category, name="category"),
    path("categories/<str:name>/", views.category_similar, name="category_similar"),
    path("listing/<int:id>", views.listing, name="listing"),
    path("watchlist/", views.watchlist, name="watchlist"),
    path("watchlist/<int:id>", views.addToWatchlist, name="add_watchlist")
]
