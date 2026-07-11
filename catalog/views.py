from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import datetime

# Create your views here.

def abigail(request: HttpRequest) -> HttpResponse:
  now = datetime.datetime.now()
  return HttpResponse("<html>"
                      "<h1>Abigail!</h1>"
                      f"<h2>Agora é: {now}</h2>"
                      "</html>"
                      )