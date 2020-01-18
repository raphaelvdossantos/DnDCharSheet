from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CharSheet
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserform

# Create your views here.


def homepage(request):
    return render(request=request,
                  template_name="main/home.html",
                  context={"Characters": CharSheet.objects.all()})


def index(request):
    return render(request,
                  "main/index.html",
                  )


def register(request):
    if request.method == "POST":
        form = NewUserform(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account Created: {username}")
            login(request, user)
            messages.info(request, f"Logged in as: {username}")
            return redirect("main:index")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}:{form.error_messages[msg]}")

    form = NewUserform
    return render(request,
                  "main/form_new_user.html",
                  context={"form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out Sucessufully.")
    return redirect("main:homepage")


def login_request(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Logged in as: {username}")
                return redirect("main:index")
            else:
                messages.error(request, "Invalid User/Password")
        else:
            messages.error(request, "Invalid User/Password")

    return render(request,
                  "main/form_login.html",
                  {"form": form})