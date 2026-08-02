from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.urls import reverse

# Create your views here.

def login_view(request: HttpRequest) -> HttpResponse:
  if request.method == "GET":
    return render(request, "accounts/login.html")
  elif request.method == "POST":
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(username=username, password=password)
    if user:
      login(request, user)
      return HttpResponseRedirect(reverse("catalog:index"))
    else:
      error_context= {
        "error": "credenciais inválidas"
      }
    return render(request, "accounts/login.html", context= error_context)