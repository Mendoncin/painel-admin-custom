from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.

def login_view(request: HttpRequest) -> HttpResponse:
  return render(request, "accounts/login.html")
