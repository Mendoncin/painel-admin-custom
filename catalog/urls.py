from django.urls import path
from catalog.views import abigail, index, LiteraryFormatsListView, BooksListViews, \
    AuthorsListViews, BookDetailViews, AuthorDetailView, LiteraryFormatsCreateView

app_name = "catalog"

urlpatterns = [
    path("abigail/<int:unique_number>/", abigail, name="abigail"),
    path("", index, name="index"),
    path("generos/", LiteraryFormatsListView.as_view(), name="lista-de-generos"),
    path("generos/create/", LiteraryFormatsCreateView.as_view(), name="criar-generos"),
    path("livros/", BooksListViews.as_view(), name="lista-de-livros"),
    path("livros/<int:pk>", BookDetailViews.as_view(), name="detalhes-livros"),
    path("autores/", AuthorsListViews.as_view(), name="lista-de-autores"),
    path("autores/<int:pk>", AuthorDetailView.as_view(), name="detalhes-autores")
]
