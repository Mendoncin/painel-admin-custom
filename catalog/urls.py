from django.urls import path
from catalog.views import abigail, index, LiteraryFormatsListView, BooksListViews, AuthorsListViews
app_name = "catalog"

urlpatterns = [
    path("abigail/<int:unique_number>/", abigail, name="abigail"),
    path("", index, name="index"),
    path("generos/", LiteraryFormatsListView.as_view(), name="lista-de-generos"),
    path("livros/", BooksListViews.as_view(), name="lista-de-livros"),
    path("autores/", AuthorsListViews.as_view(), name="lista-de-autores")
]