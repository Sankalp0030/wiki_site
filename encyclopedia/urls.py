from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>/", views.get_page, name="content"),
    path("search/", views.get_search, name="search"),
    path("add/", views.add_page, name="add"),
    path("save/", views.save_page, name="save"),
]
