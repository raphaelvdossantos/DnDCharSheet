from django.shortcuts import render, redirect
from .models import CharacterMain
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import NewUserform, CharacterMainForm
from django.views.generic import ListView, DetailView
# Create your views here.


def homepage(request):
    return render(request=request,
                  template_name="main/home.html",
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
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            if len(password1) < 7:
                messages.error(request, "Your password must have at least 8 characters")
            if password1 != password2:
                messages.error(request, "Your passwords must match")

    form = NewUserform
    return render(request,
                  "main/form_new_user.html",
                  context={"form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out Sucessufully.")
    return redirect("main:homepage")


def login_request(request):
    if not request.user.is_authenticated:
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
    else:
        return redirect("main:index")


def new_character(request):

    form = CharacterMainForm(request.POST or None)
    if form.is_valid():
        user_character = form.save(commit=False)
        user_character.user_character = request.user
        user_character.save()
        messages.info(request, "Character Created Successfully!")
        return redirect("main:index")

    return render(request,
                  "main/form_new_char.html",
                  {"form":form})


class CharacterView(ListView):
    model = CharacterMain
    template_name = "main/index.html"
    context_object_name = "all_user_characters"

    def get_queryset(self):
        return CharacterMain.objects.filter(user_character=self.request.user)


class CharacterMainView(DetailView):
    template_name = "main/char_profile.html"
    context_object_name = "selected_character"
    queryset = CharacterMain.objects.all()



