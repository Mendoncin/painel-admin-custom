from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import datetime
from .models import Book, Author

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
  return HttpResponse(
    "<html>"
    "<h1>HOME PAGE</h1>"
    "<ul>"
    f"<li>Número de Livros no catálogo: {num_books}</li>"
    f"<li>Número de Autores no catálogo: {num_author}</li>"
    "</ul>"
    "</html>"
  )