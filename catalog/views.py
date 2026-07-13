from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import datetime
from .models import Book, Author, LiteraryFormat

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