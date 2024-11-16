from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate


def home(request):
    if request.user.is_authenticated:
        return redirect("notes:note_list")
    else:
        return render(request, 'notes/home.html')

def register_view(request):
    if request.user.is_authenticated:
        return redirect("notes:note_list")
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect("notes:note_list")
    else:
        form = UserCreationForm()
    return render(request, 'users/registration/signup.html', {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("notes:note_list")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("notes:note_list")
    else:
        form = AuthenticationForm()

    return render(request, 'users/registration/login.html', {"form": form})

def logout_func(request):
    if request.method == "POST":
        logout(request)
        return redirect("notes:home")
