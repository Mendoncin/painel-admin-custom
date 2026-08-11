from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import datetime

from django.urls import reverse_lazy
from .models import Book, Author, LiteraryFormat
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def abigail(request: HttpRequest, unique_number: int) -> HttpResponse:
  now = datetime.datetime.now()
  return HttpResponse("<html>"
                      "<h1>Abigail!</h1>"
                      f"<h2>Agora é: {now}</h2>"
                      "</html>"
                      f"<h4>Número = {unique_number}</h4>"
                      )


@login_required
def index(request: HttpRequest) -> HttpResponse:
  num_books = Book.objects.count()
  num_author = Author.objects.count()
  num_literary = LiteraryFormat.objects.count()

  num_visits = request.session.get("num_visits", 0)
  request.session["num_visits"] = num_visits + 1

  context = {
    "num_books": num_books,
    "num_authors": num_author,
    "num_lit": num_literary,
    "num_visits": num_visits
  }
  return render(request, "catalog/index.html", context=context)


class LiteraryFormatsListView(LoginRequiredMixin, generic.ListView):
  model = LiteraryFormat
  template_name = "catalog/genres_list.html"
  context_object_name = "genres"


class LiteraryFormatsCreateView(LoginRequiredMixin, generic.CreateView):
  model = LiteraryFormat
  fields = "__all__"
  template_name = "catalog/genres_form.html"
  success_url = reverse_lazy("catalog:lista-de-generos")


class LiteraryFormatsUpdateView(LoginRequiredMixin, generic.UpdateView):
  model = LiteraryFormat
  fields = "__all__"
  template_name = "catalog/genres_form.html"
  success_url = reverse_lazy("catalog:lista-de-generos")


class LiteraryFormatsDeleteView(LoginRequiredMixin, generic.DeleteView):
  model = LiteraryFormat
  template_name = "catalog/genres_confirm_delete.html"
  success_url = reverse_lazy("catalog:lista-de-generos")

class BooksListViews(LoginRequiredMixin, generic.ListView):
  model = Book
  queryset = Book.objects.select_related("format")


class AuthorsListViews(LoginRequiredMixin, generic.ListView):
  model = Author


class BookDetailViews(LoginRequiredMixin, generic.DetailView):
  model = Book

"""def books_details(request: HttpRequest, pk: int) -> HttpResponse:
  book = Book.objects.get(id=pk)
  context = {
    "book": book
  }
  return render(request, "catalog/book_detail.html", context=context)"""


class AuthorDetailView(LoginRequiredMixin, generic.DetailView):
  model = Author
