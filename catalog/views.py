from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import datetime
from .models import Book, Author, LiteraryFormat
from django.views import generic


def abigail(request: HttpRequest, unique_number: int) -> HttpResponse:
  now = datetime.datetime.now()
  return HttpResponse("<html>"
                      "<h1>Abigail!</h1>"
                      f"<h2>Agora é: {now}</h2>"
                      "</html>"
                      f"<h4>Número = {unique_number}</h4>"
                      )


def index(request: HttpRequest) -> HttpResponse:
  num_books = Book.objects.count()
  num_author = Author.objects.count()
  num_literary = LiteraryFormat.objects.count()
  context = {
    "num_books": num_books,
    "num_authors": num_author,
    "num_lit": num_literary
  }
  return render(request, "catalog/index.html", context=context)


class LiteraryFormatsListView(generic.ListView):
  model = LiteraryFormat
  template_name = "catalog/genres_list.html"
  context_object_name = "genres"


class BooksListViews(generic.ListView):
  model = Book
  queryset = Book.objects.select_related("format")


class AuthorsListViews(generic.ListView):
  model = Author


class BookDetailViews(generic.DetailView):
  model = Book

"""def books_details(request: HttpRequest, pk: int) -> HttpResponse:
  book = Book.objects.get(id=pk)
  context = {
    "book": book
  }
  return render(request, "catalog/book_detail.html", context=context)"""