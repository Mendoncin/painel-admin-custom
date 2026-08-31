from django.urls import path
from catalog.views import abigail, index, LiteraryFormatsListView, BooksListViews, \
    AuthorsListViews, BookDetailViews, AuthorDetailView, LiteraryFormatsCreateView, \
    LiteraryFormatsUpdateView, LiteraryFormatsDeleteView, AuthorCreateView, BookCreateView, BookUpdateView

app_name = "catalog"

urlpatterns = [
    path("abigail/<int:unique_number>/", abigail, name="abigail"),
    path("", index, name="index"),
    path("generos/", LiteraryFormatsListView.as_view(), name="lista-de-generos"),
    path("generos/create/", LiteraryFormatsCreateView.as_view(), name="criar-generos"),
    path("generos/<int:pk>/update/", LiteraryFormatsUpdateView.as_view(), name="atualizar-generos"),
    path("generos/<int:pk>/delete/", LiteraryFormatsDeleteView.as_view(), name="excluir-generos"),
    path("livros/", BooksListViews.as_view(), name="lista-de-livros"),
    path("livros/create/", BookCreateView.as_view(), name="criar-livros"),
    path("livros/<int:pk>", BookDetailViews.as_view(), name="detalhes-livros"),
    path("livros/<int:pk>/update/", BookUpdateView.as_view(), name="atualizar-livros"),
    path("autores/", AuthorsListViews.as_view(), name="lista-de-autores"),
    path("autores/<int:pk>", AuthorDetailView.as_view(), name="detalhes-autores"),
    path("autores/create/", AuthorCreateView.as_view(), name="criar-autores")
]
