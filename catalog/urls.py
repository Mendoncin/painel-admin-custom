from django.urls import path
from catalog.views import abigail, index, list_genres

app_name = "catalog"

urlpatterns = [
    path("abigail/<int:unique_number>/", abigail, name="abigail"),
    path("", index, name="index"),
    path("generos/", list_genres, name="lista-de-generos")
]